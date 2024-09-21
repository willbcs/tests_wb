from PySimpleGUI import PySimpleGUI as sg
import requests

sg.theme('Reddit')

API_KEY = '69ddec2d6c8acd5a481e1c6959e64262'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

cidades = [
    # Capitais do Mundo
    'Abu Dhabi', 'Accra', 'Addis Ababa', 'Algiers', 'Andorra la Vella', 'Ankara', 'Antananarivo', 'Asunción', 'Athens', 'Baghdad',
    'Baku', 'Bamako', 'Bangkok', 'Banjul', 'Bucharest', 'Budapest', 'Buenos Aires', 'Cairo', 'Canberra', 'Caracas',
    'Castries', 'Chisinau', 'Colombo', 'Copenhagen', 'Dakar', 'Damascus', 'Dhaka', 'Dili', 'Dodoma', 'Doha',
    'Dubai', 'Dushanbe', 'Edinburgh', 'Jakarta', 'Jerusalem', 'Juba', 'Kabul', 'Kampala', 'Kathmandu', 'Khartoum',
    'Kiev', 'Kigali', 'Kingston', 'Kinshasa', 'Kuala Lumpur', 'Kuwait City', 'La Paz', 'Libreville', 'Lima', 'Lisbon',
    'Ljubljana', 'Lome', 'London', 'Luanda', 'Lusaka', 'Madrid', 'Majuro', 'Malabo', 'Male', 'Managua',
    'Manama', 'Mansoura', 'Maputo', 'Marigot', 'Minsk', 'Mogadishu', 'Monaco', 'Monrovia', 'Montevideo', 'Moroni',
    'Moscow', 'Muscat', 'Nairobi', 'Nassau', 'New Delhi', 'Nouakchott', 'Oslo', 'Ottawa', 'Paris', 'Podgorica',
    'Port Moresby', 'Port au Prince', 'Porto-Novo', 'Prague', 'Rabat', 'Reykjavik', 'Riga', 'Rome', 'San Salvador',
    'Sana', 'São Tomé', 'Sarajevo', 'Seoul', 'Singapore', 'Sofia', 'Stockholm', 'Sucre', 'Tallinn', 'Tashkent',
    'Tbilisi', 'Tokyo', 'Tunis', 'Ulaanbaatar', 'Vaduz', 'Valletta', 'Vatican City', 'Vienna', 'Vientiane', 'Vilnius',
    'Warsaw', 'Washington, D.C.', 'Wellington', 'Yamoussoukro', 'Yaoundé', 'Zagreb', 'Zurich',
    # Capitais do Brasil
    'Brasília', 'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Fortaleza', 'Curitiba', 'Recife', 'Porto Alegre', 'Manaus',
    'Belém', 'Goiânia', 'São Luís', 'Maceió', 'Natal', 'João Pessoa', 'Campo Grande', 'Teresina', 'Aracaju', 'Vitória',
    # Principais Cidades do Brasil
    # Região Norte
    'Boa Vista', 'Macapá', 'Rio Branco', 'Palmas', 'Itacoatiara', 'Santarem', 'Marabá', 'Parintins', 'Humaitá', 'Porto Velho',
    # Região Nordeste
    'Aracaju', 'Campina Grande', 'Feira de Santana', 'Juazeiro', 'Mossoró', 'São Luís', 'Teresina', 'Ilhéus', 'Barreiras', 'Cruz das Almas',
    # Região Centro-Oeste
    'Aparecida de Goiânia', 'Anápolis', 'Dourados', 'Rondonópolis', 'Várzea Grande', 'Chapadão do Sul', 'Luziania', 'Araxá', 'Uberlândia', 'Sorriso',
    # Região Sudeste
    'São José dos Campos', 'Santos', 'Sorocaba', 'Campinas', 'Piracicaba', 'Jundiaí', 'Bauru', 'São Bernardo do Campo', 'São Caetano do Sul', 'Diadema',
    # Região Sul
    'Joinville', 'Blumenau', 'Caxias do Sul', 'Ponta Grossa', 'Maringá', 'Londrina', 'Chapecó', 'Ijuí', 'Santa Maria', 'Pelotas'
]

def obter_clima_tempo(cidade):
    url = BASE_URL + f"q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    #Requisita HTTP
    resposta = requests.get(url)
    #Converter em JSON
    dados = resposta.json()

    if resposta.status_code == 200 and dados['cod'] == 200:
        longitude = dados["coord"]["lon"]
        latitude = dados["coord"]["lat"]
        condicao = dados["weather"][0]["main"]
        descricao = dados["weather"][0]["description"]
        temperatura = dados["main"]["temp"]
        sensação_termica = dados["main"]["feels_like"]
        temp_min = dados["main"]["temp_min"]
        temp_max = dados["main"]["temp_max"]
        humidade = dados["main"]["humidity"]
        velocidade_vento = dados["wind"]["speed"]
        pais_sigla = dados["sys"]["country"]
        local_nome = dados["name"]

        return longitude, latitude, condicao, descricao, temperatura, sensação_termica, temp_min, temp_max, humidade, velocidade_vento, pais_sigla, local_nome
    else:
        return None
    
color = 'lightgrey'   
layout = [

    [sg.Text('Escolha uma cidade: ', background_color = color, relief=sg.RELIEF_RIDGE, font=('Default', 10, 'bold'), justification='center')], 
    
    [sg.Combo(cidades, key = '-CIDADE-', readonly=True), sg.Button('Buscar', button_color = ('white', 'blue'), font= ('default', 10, 'bold')), sg.Button('Fechar', button_color = ('white', 'blue'), font= ('default', 10, 'bold'))],
  
    [sg.Text('', size = (1,1), background_color = color)],
  
    [sg.Text('Longitude:', size=(15, 1), relief=sg.RELIEF_RIDGE, background_color = color, font=('Default', 10, 'bold'), justification='center'), sg.Text('', key='-LONGITUDE-', background_color = color)],
 
    [sg.Text('Latitude:', size=(15, 1), relief=sg.RELIEF_RIDGE, font=('Default', 10, 'bold'), justification='center', background_color = color), sg.Text('', key='-LATITUDE-', background_color = color)],
  
    [sg.Text('Condição:', size=(15, 1), relief=sg.RELIEF_RIDGE, font=('Default', 10, 'bold'), justification='center', background_color = color), sg.Text('', key='-CONDICAO-', background_color = color)],
   
    [sg.Text('Descrição:', size=(15, 1), relief=sg.RELIEF_RIDGE, font=('Default', 10, 'bold'), justification='center', background_color = color), sg.Text('', key='-DESCRICAO-', background_color = color)],
    
    [sg.Text('', size=(1,1), background_color = color)],
    
    [sg.Text('Temperatura:', size=(15, 1), font=('Default', 14, 'bold'), justification='center', background_color = color, relief=sg.RELIEF_RIDGE,), sg.Text('', key='-TEMPERATURA-', font=('Default', 14), background_color = color)],
    
    [sg.Text('', size=(1,1), background_color = color)],
    
    [sg.Text('Sensação Térmica:', size=(15, 1),relief=sg.RELIEF_RIDGE, font=('Default', 10, 'bold'), justification='center', background_color = color), sg.Text('', key='-SENSACAO_TERM-', background_color = color)],
    
    [sg.Text('Temp Min:', size=(15, 1), relief=sg.RELIEF_RIDGE, font=('Default', 10, 'bold'), justification='center', background_color = color), sg.Text('', key='-TEMP_MIN-', background_color = color)],
    
    [sg.Text('Temp Max:', size=(15, 1), relief=sg.RELIEF_RIDGE, font=('Default', 10, 'bold'), justification='center', background_color = color), sg.Text('', key='-TEMP_MAX-', background_color = color)],
    
    [sg.Text('Humidade:', size=(15, 1), relief=sg.RELIEF_RIDGE, font=('Default', 10, 'bold'), justification='center', background_color = color), sg.Text('', key='-HUMIDADE-', background_color = color)],
    
    [sg.Text('Veloc. do Vento:', size=(15, 1), relief=sg.RELIEF_RIDGE, font=('Default', 10, 'bold'), justification='center', background_color = color), sg.Text('', key='-VENTO-', background_color = color)],
    
    [sg.Text('País:', size=(15, 1), relief=sg.RELIEF_RIDGE, font=('Default', 10, 'bold'), justification='center', background_color = color), sg.Text('', key='-PAIS-', background_color = color)],
    
    [sg.Text('Local:', size=(15, 1), relief=sg.RELIEF_RIDGE, font=('Default', 10, 'bold'), justification='center', background_color = color), sg.Text('', key='-LOCAL-', background_color = color)]
]

janela = sg.Window("Dados do Clima", layout, size=(320, 500), finalize=True, grab_anywhere=True, background_color = color)
janela.move_to_center()


while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Fechar':
        break

    if eventos == "Buscar":
        cidades = valores['-CIDADE-']
        if cidades:
            dados_clima = obter_clima_tempo(cidades)
            if dados_clima is None:
                sg.popup(f'Erro: Dados não encontrados. Tente novamente mais tarde!')
            else:
                janela['-LONGITUDE-'].update(f"{dados_clima[0]}°", font =('Default', 10, 'bold'))
                janela['-LATITUDE-'].update(f"{dados_clima[1]}°", font =('Default', 10, 'bold'))
                janela['-CONDICAO-'].update(dados_clima[2], font =('Default', 10, 'bold'))
                janela['-DESCRICAO-'].update(dados_clima[3], font =('Default', 10, 'bold'))
                janela['-TEMPERATURA-'].update(f"{dados_clima[4]}°C", font =('Default', 14, 'bold'))
                janela['-SENSACAO_TERM-'].update(f"{dados_clima[5]}°C", font =('Default', 10, 'bold'))
                janela['-TEMP_MIN-'].update(f"{dados_clima[6]}°C", font =('Default', 10, 'bold'))
                janela['-TEMP_MAX-'].update(f"{dados_clima[7]}°C", font =('Default', 10, 'bold'))
                janela['-HUMIDADE-'].update(f"{dados_clima[8]}%", font =('Default', 10, 'bold'))
                janela['-VENTO-'].update(f"{dados_clima[9]}m/s", font =('Default', 10, 'bold'))
                janela['-PAIS-'].update(dados_clima[10], font =('Default', 10, 'bold'))
                janela['-LOCAL-'].update(dados_clima[11], font =('Default', 10, 'bold'))               

janela.close()