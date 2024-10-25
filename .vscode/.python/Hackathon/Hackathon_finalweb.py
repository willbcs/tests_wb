import requests
import pyodbc
from bs4 import BeautifulSoup
import re
from flask import Flask, render_template, redirect, url_for, request

# Configurações do banco de dados
DRIVER = 'ODBC Driver 17 for SQL Server'
SERVER = 'DESKTOP-8FCL3JR'
DATABASE = 'hackathon'
trusted_connection = 'yes'

# URL da página que você deseja fazer scraping
url = "https://articket.com.br/busca?q=Santos"

app = Flask(__name__)

# Função para conectar ao banco de dados SQL Server e criar a tabela 'eventos'
def cria_banco():
    try:
        conn = pyodbc.connect(f'DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
        cursor = conn.cursor()

        # Criação da tabela se não existir
        cursor.execute(''' 
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='eventos' AND xtype='U')
            CREATE TABLE eventos (
                id INT PRIMARY KEY IDENTITY(1,1),
                titulo NVARCHAR(MAX),
                data_hora NVARCHAR(MAX),
                local NVARCHAR(MAX),
                valor NVARCHAR(MAX),
                descricao NVARCHAR(MAX),
                compra NVARCHAR(MAX)
            )
        ''')
        conn.commit()
    except pyodbc.Error as e:
        print(f"Erro ao conectar ou criar banco de dados: {e}")
    finally:
        conn.close()

# Função para fazer scraping da página
def conexao_pagina(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.content
        else:
            print(f"Erro ao acessar a página: {resposta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro durante a requisição: {e}")
    return None

def links_info(soup):
    divs = soup.find_all('div', class_='mt-5 mb-5')
    links = {div.find('a', href=True)['href'] for div in divs}  # Usando um set para evitar duplicatas
    return list(links)  # Retorna uma lista sem duplicatas

def lista_info(link):
    evento_resposta = requests.get(link)
    if evento_resposta.status_code == 200:
        eventos_soup = BeautifulSoup(evento_resposta.content, 'html.parser')

        titulo = eventos_soup.find('h1', class_='flex text-center justify-center text-2xl font-medium tracking-wide text-white lg:text-4xl').get_text(strip=True)
        data_hora = eventos_soup.find('span', class_="m-0 text-red-300").get_text(strip=True)
        local = eventos_soup.find('span', class_="m-1").get_text(strip=True)
        descricao = eventos_soup.find('div', class_="px-8 py-4 mx-auto w-full col-span-2").get_text(strip=True)

        # Limitar a descrição a um máximo de 200 caracteres
        limite = 200
        if len(descricao) > limite:
            descricao = descricao[:limite] + "..."

        # Procurar o primeiro valor no formato "R$XX.XX"
        html_texto = eventos_soup.get_text()
        encontrar_preco = re.search(r'R\$\s*\d{1,3}(?:\.\d{3})*\.\d{2}', html_texto)
        if encontrar_preco:
            valor = encontrar_preco.group(0)
        else:
            valor = "Não disponível"

        return {             
            'titulo': titulo,
            'data_hora': data_hora,
            'local': local,
            'valor': valor,
            'descricao': descricao,
            'compra': link
        }
    else:
        print(f"Erro ao acessar o link do evento: {evento_resposta.status_code}")
    return None

def insere_evento(evento):
    try:
        conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
        cursor = conn.cursor()

        # Verifica se o evento já existe usando o link de compra
        cursor.execute('SELECT COUNT(*) FROM eventos WHERE compra = ?', 
                       (evento['compra'],))
        existe = cursor.fetchone()[0]

        if existe == 0:  # Se não existe, insere
            cursor.execute(''' 
                INSERT INTO eventos (titulo, data_hora, local, valor, descricao, compra)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (evento['titulo'], evento['data_hora'], evento['local'], evento['valor'], evento['descricao'], evento['compra']))
            conn.commit()

            # Recupera o ID do evento inserido
            cursor.execute('SELECT @@IDENTITY')
            evento_id = cursor.fetchone()[0]

            print(f"Evento '{evento['titulo']}' inserido no banco de dados.")
            return evento_id  # Retorna o ID do evento inserido
        else:
            print(f"Evento '{evento['titulo']}' já existe no banco de dados.")
            return None  # Se o evento já existe, retorna None

    except pyodbc.Error as e:
        print(f"Erro ao conectar no banco de dados: {e}")
    finally:
        conn.close()


@app.route('/eventos')
def eventos():
    sort = request.args.get('sort', 'id')  # Obtém o parâmetro de ordenação, padrão é 'id'
    
    # Conectar ao banco de dados e buscar eventos
    try:
        conn = pyodbc.connect(f'DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
        cursor = conn.cursor()

        # Verifica se a ordenação é para a coluna 'data_hora'
        if sort == 'data_hora':
            query = """
                SELECT * FROM eventos
                ORDER BY CONVERT(datetime, SUBSTRING(data_hora, 1, 10), 103)
            """
        else:
            # Para 'id' ou outras colunas, ordem padrão
            query = f"SELECT * FROM eventos ORDER BY {sort}"

        cursor.execute(query)
        eventos = cursor.fetchall()
        
        # Estruturar os dados para passar para o template
        eventos_list = []
        for evento in eventos:
            eventos_list.append({
                'id': evento[0],
                'titulo': evento[1],
                'data_hora': evento[2],
                'local': evento[3],
                'valor': evento[4],
                'descricao': evento[5],
                'compra': evento[6]
            })
        
        return render_template('eventos.html', eventos=eventos_list)
    except pyodbc.Error as e:
        print(f"Erro ao conectar no banco de dados: {e}")
    finally:
        conn.close()


@app.route('/')
def index():
    return redirect(url_for('eventos'))

def main():
    # Cria o banco de dados e a tabela
    cria_banco()

    # Verifica se já existem eventos no banco
    conn = pyodbc.connect(f'DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM eventos")
    eventos_count = cursor.fetchone()[0]
    
    if eventos_count == 0:
        # Fazer scraping e inserir eventos no banco de dados
        pag_conex = conexao_pagina(url)
        if pag_conex:
            soup = BeautifulSoup(pag_conex, 'html.parser')
            evento_links = links_info(soup)

            print("Buscando...")
            eventos_inseridos = []  # Lista para armazenar eventos inseridos
            for link in evento_links:
                evento = lista_info(link)
                if evento:
                    evento_id = insere_evento(evento)
                    if evento_id:  # Se o evento foi inserido
                        eventos_inseridos.append(evento)  # Adiciona o evento à lista

            if eventos_inseridos:
                print(f"{len(eventos_inseridos)} eventos inseridos no banco de dados.")

    # Iniciar o aplicativo Flask
    app.run(debug=True)

if __name__ == '__main__':
    main()