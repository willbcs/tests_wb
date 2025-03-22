Hackathon - Web Scraping e Banco de Dados

Este projeto realiza web scraping de eventos na plataforma Articket, armazena os dados em um banco de dados SQL Server e exibe os eventos em uma interface web usando Flask.

📂 Estrutura do Projeto

📂 Hackathon/
│── 📂 templates/
│   ├── eventos.html  # Página HTML para exibição dos eventos
├── Hackathon_finalweb.py  # Script principal do projeto

🛠️ Tecnologias Utilizadas

Python 3.x

Flask

Requests

BeautifulSoup4

PyODBC

SQL Server

⚙️ Configuração e Instalação

Clone este repositório:

git clone https://github.com/willbcs/tests_wb.git
cd tests_wb/.vscode/.python/exercicios/Hackathon

Instale as dependências:

pip install flask requests beautifulsoup4 pyodbc

Configure o banco de dados SQL Server:

Atualize SERVER e DATABASE no script para corresponder às configurações do seu banco.

O script criará a tabela eventos automaticamente, caso não exista.

🚀 Como Executar

Inicie a aplicação Flask:

python Hackathon_finalweb.py

Acesse no navegador:

http://127.0.0.1:5000/eventos

📌 Funcionalidades

Web Scraping: Coleta informações de eventos da plataforma Articket.

Banco de Dados: Armazena os eventos no SQL Server evitando duplicatas.

Interface Web: Exibe os eventos cadastrados no banco.

Ordenação: Permite visualizar eventos ordenados por ID ou data.

📬 Contato

Caso tenha dúvidas, entre em contato pelo e-mail: willbc.silva@gmail.com

Desenvolvido com 💻 por William Bruno