import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Análise ENEM 2021 - BA",
    page_icon="📚",
    layout="wide"
)

# Carregamento dos dados
#A URL contendo o csv com os dados: https://drive.google.com/drive/folders/1NKuM2jtJr8vq1K3gXsfOuH6Bs58xLnqU?hl=pt-br
@st.cache_data
def load_data():
    return pd.read_csv(r'C:\Users\Myrath\Documents\Dados\dados_enem_2021_BA.csv') # Substitua pelo caminho correto onde você colocou o arquivo CSV

try:
    df = load_data()
except FileNotFoundError:
    st.error("Arquivo não encontrado. Verifique o caminho do arquivo.")
    st.stop()

# Renomeação das colunas para termos mais amigáveis
df = df.rename(columns={
    'TP_ESCOLA': 'Tipo de Escola',
    'NU_NOTA_MT': 'Nota Matemática',
    'NU_NOTA_LC': 'Nota Linguagens',
    'NU_NOTA_REDACAO': 'Nota Redação',
    'NO_MUNICIPIO_PROVA': 'Município'
})

# Mapeamento dos valores para termos mais descritivos
df['Tipo de Escola'] = df['Tipo de Escola'].replace({
    1: 'Não respondeu',
    2: 'Pública',
    3: 'Particular'
})

# Sidebar - Filtros
st.sidebar.header("Filtros")
municipios = ['Todos'] + sorted(df['Município'].unique().tolist())
municipio_selecionado = st.sidebar.selectbox("Selecione um município:", municipios)

if municipio_selecionado != 'Todos':
    df_filtro = df[df['Município'] == municipio_selecionado]
else:
    df_filtro = df.copy()

# Layout principal
st.title("Análise do ENEM 2021 - Bahia")

# Gráfico 1: Distribuição do tipo de escola
st.header("1. Distribuição dos Candidatos por Tipo de Escola")
contagem_escolas = df_filtro['Tipo de Escola'].value_counts().reset_index()
contagem_escolas.columns = ['Tipo de Escola', 'Quantidade']

fig1 = px.pie(
    contagem_escolas,
    names='Tipo de Escola',
    values='Quantidade',
    color='Tipo de Escola',
    color_discrete_map={'Pública': '#2ecc71', 'Particular': '#e74c3c', 'Não respondeu': '#3498db'}
)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Top municípios com mais candidatos
st.header("2. Municípios com Maior Número de Candidatos")
top_municipios = df['Município'].value_counts().nlargest(15).reset_index()
top_municipios.columns = ['Município', 'Quantidade']

fig2 = px.bar(
    top_municipios,
    x='Quantidade',
    y='Município',
    orientation='h',
    color='Quantidade',
    color_continuous_scale='reds'
)
st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Distribuição das notas de redação
st.header("3. Distribuição das Notas de Redação")
df_redacao = df_filtro[df_filtro['Nota Redação'].notna() & (df_filtro['Nota Redação'] > 0)]

fig3 = px.histogram(
    df_redacao,
    x='Nota Redação',
    nbins=20,
    color_discrete_sequence=['#9b59b6']
)
st.plotly_chart(fig3, use_container_width=True)

# Gráfico 4: Melhores desempenhos em Matemática
st.header("4. Melhores Desempenhos em Matemática por Município")
notas_matematica = (
    df_filtro.groupby('Município')['Nota Matemática']
    .mean()
    .nlargest(10)
    .reset_index()
)

fig4 = px.bar(
    notas_matematica,
    x='Nota Matemática',
    y='Município',
    orientation='h',
    color='Nota Matemática',
    color_continuous_scale='greens'
)
st.plotly_chart(fig4, use_container_width=True)

# Gráfico 5: Comparação de desempenho por tipo de escola
st.header("5. Comparação de Desempenho por Tipo de Escola")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Desempenho em Matemática")
    fig5a = px.box(
        df_filtro,
        x='Tipo de Escola',
        y='Nota Matemática',
        color='Tipo de Escola',
        color_discrete_map={'Pública': '#2ecc71', 'Particular': '#e74c3c', 'Não respondeu': '#3498db'}
    )
    st.plotly_chart(fig5a, use_container_width=True)

with col2:
    st.subheader("Desempenho em Linguagens")
    fig5b = px.box(
        df_filtro,
        x='Tipo de Escola',
        y='Nota Linguagens',
        color='Tipo de Escola',
        color_discrete_map={'Pública': '#2ecc71', 'Particular': '#e74c3c', 'Não respondeu': '#3498db'}
    )
    st.plotly_chart(fig5b, use_container_width=True)

    #Abra a pasta do projeto e use o comando streamlit run dash_enem.py no terminal para executar o dashboard.
