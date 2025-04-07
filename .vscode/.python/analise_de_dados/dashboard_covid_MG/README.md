Dashboard de Análise de Óbitos por COVID-19 em Minas Gerais (ANO DE 2020)

Este projeto é um dashboard interativo para análise de dados de óbitos confirmados por COVID-19 no estado de Minas Gerais, exibindo informações sobre distribuição por idade, sexo, comorbidades, faixas etárias e municípios.

📂 Estrutura do Projeto

📂 dashboard_covid_mg/  
│-- OBITOS_CONF_COVID-19_MG.csv  # Base de dados (delimitado por ";", encoding Latin1)  
│-- dash_covid_MG.py             # Script principal do dashboard  
│-- requirements.txt             # Dependências do projeto  
│-- README.md                    # Este arquivo  

🛠️ Tecnologias Utilizadas
Python 3.8+
Streamlit (framework para visualização)
Pandas (manipulação de dados)
Plotly Express (visualização gráfica)

⚙️ Configuração e Instalação
Clone este repositório
Crie e ative um ambiente virtual (recomendado):
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instale as dependências:
pip install -r requirements.txt

📋 Arquivo requirements.txt
streamlit==1.28.0
pandas==2.0.3
plotly==5.15.0

🚀 Como Executar
Execute o dashboard com o comando:
streamlit run app.py
O dashboard será aberto automaticamente no navegador padrão na porta 8501.

📊 Funcionalidades Principais
✅ Filtro por cidade: Selecione um município específico ou visualize todos.

📈 Visualizações interativas:

Distribuição por sexo (gráfico de pizza)

Comorbidades associadas (gráfico de pizza)

Distribuição de idade (histograma)

Óbitos por faixa etária (gráfico de barras)

Evolução mensal de óbitos (gráfico de linha)

Top 15 cidades por média de idade (gráfico de barras horizontais)

Top 15 cidades com mais óbitos (gráfico de barras horizontais)

🎨 Layout responsivo: Adapta-se a diferentes tamanhos de tela.

📌 Estrutura dos Dados
O arquivo CSV deve conter as seguintes colunas (ajuste conforme seu dataset):

DATA_DO_ÓBITO: Data do óbito (formato dd/mm/YYYY)

MUNICÍPIO_DE_RESIDÊNCIA: Nome do município

IDADE: Idade do falecido (numérico)

SEXO: Sexo (M ou F, convertido para "Masculino"/"Feminino")

COMORBIDADE: Condições pré-existentes (ex.: "Diabetes", "Hipertensão")

🔧 Personalização
Para adaptar o dashboard aos seus dados:

Modifique o caminho do arquivo CSV em app.py.

Ajuste os nomes das colunas se necessário.

Altere as cores padrão nos gráficos editando color_discrete_sequence.

📬 Contato
Para dúvidas ou sugestões:

E-mail: willbc.silva@gmail.com

LinkedIn: William Bruno Carlos Silva

Desenvolvido com 💻 por William Bruno.