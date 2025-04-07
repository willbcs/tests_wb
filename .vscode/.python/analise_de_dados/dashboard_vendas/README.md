Dashboard de Análise de Vendas
Este projeto é um dashboard interativo para análise de dados de vendas, exibindo informações sobre faturamento por período, loja, produto e forma de pagamento.

📂 Estrutura do Projeto
📂 dashboard_vendas/
│-- dados_vendas.csv         # Base de dados das vendas (delimitado por ;, encoding ISO-8859-1)
│-- dash.py                  # Script principal do dashboard
│-- requirements.txt         # Dependências do projeto
│-- README.md                # Este arquivo

🛠️ Tecnologias Utilizadas
Python 3.8+
Streamlit (framework para visualização)
Pandas (manipulação de dados)
Plotly Express (visualização gráfica)

⚙️ Configuração e Instalação

Clone este repositório:
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
streamlit run dash.py

O dashboard será aberto automaticamente no seu navegador padrão na porta 8501.

📊 Funcionalidades Principais
Filtro por mês: Selecione um período específico para análise

Visualizações interativas:

Faturamento diário por loja (gráfico de barras)

Faturamento por produto (gráfico de barras horizontais)

Comparativo entre lojas (gráfico de barras)

Distribuição por formas de pagamento (gráfico de pizza)

Layout responsivo: Adapta-se a diferentes tamanhos de tela

📌 Estrutura dos Dados
O arquivo CSV deve conter as seguintes colunas:

DATA_VENDA: Data da venda (formato datetime)

LOJA: Identificação da loja

PRODUTO: Nome do produto vendido

VALOR_TOTAL: Valor da venda

FORMA_PAGAMENTO: Método de pagamento utilizado

🔧 Personalização
Para adaptar o dashboard aos seus dados:

Modifique o caminho do arquivo CSV em dash.py

Ajuste os nomes das colunas se necessário

Altere as cores padrão nos gráficos editando os parâmetros color_discrete_sequence

📬 Contato
Para dúvidas ou sugestões, entre em contato:

E-mail: willbc.silva@gmail.com

LinkedIn: William Bruno Carlos Silva

Desenvolvido com 💻 por William Bruno