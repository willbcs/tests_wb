import pandas as pd
import plotly.express as px
import streamlit as st

# CONFIGURAR A PÁGINA
st.set_page_config(
    page_title="Análise de Filmes IMDB",
    layout="wide",
    page_icon="🎬"
    )
st.title("🎬 Painel de Análise de Filmes (IMDB)")

# CARREGAR OS DADOS!
@st.cache_data
def carregar_dados():
    df = pd.read_csv("IMDB-Movie-Data.csv")

    # removeu colunas indesejadas
    df = df.drop(columns=['Rank', 'Description'], errors='ignore')

    # traduzir os nomes das colunas
    traducoes = {
        'Title': 'TÍTULO',
        'Genre': 'GÊNERO',
        'Director': 'DIRETOR',
        'Actors': 'ATORES',
        'Year': 'ANO',
        'Runtime (Minutes)': 'DURAÇÃO (MIN)',
        'Rating': 'AVALIAÇÃO',
        'Votes': 'VOTOS',
        'Revenue (Millions)': 'BILHETERIA (MILHÕES $)',
        'Metascore': 'METASCORE'
    }

    # Aqui aplicarei as traduções e padronizei nomes
    df = df.rename(columns=traducoes)
    df.columns = df.columns.str.upper()

    # Converter a coluna bilheteria para números
    if "BILHETERIA (MILHÕES $)" in df.columns:
        df["BILHETERIA (MILHÕES $)"] = pd.to_numeric(df["BILHETERIA (MILHÕES $)"], errors="coerce")
    
    return df

df = carregar_dados()

# SIDEBAR (FILTROS)
st.sidebar.header("Filtros")

#Filtros por ano
ano_min = int(df["ANO"].min())
ano_max = int(df["ANO"].max())
ano_selecionado = st.sidebar.slider(
    "Selecionar o intervalo de anos",
    min_value = ano_min,
    max_value = ano_max,
    value = (ano_min, ano_max) 
)

# Filtro por gênero de filme
generos = ["TODOS"] + sorted(df["GÊNERO"].str.split(",").explode().str.strip().unique())
genero_selecionado = st.sidebar.selectbox("Selecione o gênero", generos)

# Filtro de avaliação
nota_min = float(df["AVALIAÇÃO"].min())
nota_max = float(df["AVALIAÇÃO"].max())
nota_selecionada = st.sidebar.slider(
    "Selecione a nota",
    min_value = nota_min,
    max_value = nota_max,
    value = nota_min
)

# Filtro por ano
df_filtrado = df[
    (df['ANO'] >= ano_selecionado[0]) &
    (df['ANO'] <= ano_selecionado[1]) &
    (df['AVALIAÇÃO'] >= nota_selecionada)
]

if genero_selecionado != "TODOS":
    df_filtrado = df_filtrado[df.filtrado["GÊNERO"].str.contains(genero_selecionado)]

# EXIBIÇÃO DOS DADOS COMPLETOS (ORDENADO POR BILHETERIA)
st.subheader("📊 Dados Completos (Ordenados por Bilheteria)")
st.dataframe(
    df_filtrado.sort_values("BILHETERIA (MILHÕES $)", ascending=False),
    height=300,
    use_container_width=True
)

# GRÁFICOS
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)

#GRÁFICO 1: Top 15 Maiores Bilheterias
top_bilheteria = df_filtrado.nlargest(15, "BILHETERIA (MILHÕES $)")
fig1 = px.bar(
    top_bilheteria,
    x = "TÍTULO",
    y = "BILHETERIA (MILHÕES $)",
    title = "🏆 Top 15 Maiores Bilheterias (US$ Mi)",
    color = "BILHETERIA (MILHÕES $)",
    color_continuous_scale = "Viridis"
)
col1.plotly_chart(fig1, use_container_width = True
)

# GRÁFICO 2: Bilheteria Média por Ano 
media_bilheteria_ano = df_filtrado.groupby("ANO")["BILHETERIA (MILHÕES $)"].mean().reset_index()
fig_bilheteria_ano = px.line(
    media_bilheteria_ano,
    x="ANO",
    y="BILHETERIA (MILHÕES $)",
    title="📈 Bilheteria Média por Ano",
    markers=True
)
col3.plotly_chart(fig_bilheteria_ano, use_container_width=True)

# GRÁFICO 3: Top 15 Melhores Metascores
top_metascore = df_filtrado.nlargest(15, "METASCORE")
fig2 = px.bar(
    top_metascore,
    x="TÍTULO",
    y="METASCORE",
    title="🎯 Top 15 Melhores Metascores",
    color="METASCORE",
    color_continuous_scale="Blues"
)
col4.plotly_chart(fig2, use_container_width=True)

# GRÁFICO 4: Top 15 Melhores Ratings
top_rating = df_filtrado.nlargest(15, "AVALIAÇÃO")
fig3 = px.bar(
    top_rating,
    x="TÍTULO",
    y="AVALIAÇÃO",
    title="⭐ Top 15 Melhores Avaliações (IMDB)",
    color="AVALIAÇÃO",
    color_continuous_scale="Greens"
)
col5.plotly_chart(fig3, use_container_width=True)

# GRÁFICO 5: Avaliação x Metascore
fig_avaliacao_metascore = px.scatter(
    df_filtrado,
    x="AVALIAÇÃO",
    y="METASCORE",
    size="VOTOS",
    color="ANO",
    title="🎯 Avaliação vs Metascore (Tamanho = Votos)",
    hover_data=["TÍTULO"]
)
col6.plotly_chart(fig_avaliacao_metascore, use_container_width=True)

# GRÁFICO 6: Distribuição por GÊNERO
genero_counts = df_filtrado["GÊNERO"].str.split(",").explode().str.strip().value_counts().head(10)
fig_genero = px.pie(
    names=genero_counts.index,
    values=genero_counts.values,
    title="🎭 Distribuição dos Gêneros (Top 10)",
    hole=0.4  # gráfico de rosca
)
col7.plotly_chart(fig_genero, use_container_width=True)

# GRÁFICO 7: Top 15 Filmes Mais Longos
top_runtime = df_filtrado.nlargest(15, "DURAÇÃO (MIN)")
fig4 = px.bar(
    top_runtime,
    x="TÍTULO",
    y="DURAÇÃO (MIN)",
    title="⏳ Top 15 Filmes Mais Longos (Minutos)",
    color="DURAÇÃO (MIN)",
    color_continuous_scale="Oranges"
)
col8.plotly_chart(fig4, use_container_width=True)

# GRÁFICO 8: Top 15 Bilheterias em Animação
top_animacao = df_filtrado[df_filtrado["GÊNERO"].str.contains("Animation")].nlargest(15, "BILHETERIA (MILHÕES $)")
fig5 = px.bar(
    top_animacao,
    x="TÍTULO",
    y="BILHETERIA (MILHÕES $)",
    title="🎨 Top 15 Bilheterias em Animação (US$ Mi)",
    color="BILHETERIA (MILHÕES $)",
    color_continuous_scale="Purples"
)
col2.plotly_chart(fig5, use_container_width=True)

# GRÁFICO 9: Top 10 Diretores com Mais Filmes
top_diretores = df_filtrado["DIRETOR"].value_counts().head(10).reset_index()
top_diretores.columns = ["DIRETOR", "FILMES"]
fig6 = px.bar(
    top_diretores,
    x="DIRETOR",
    y="FILMES",
    title="🎬 Top 10 Diretores com Mais Filmes",
    color="FILMES",
    color_continuous_scale="Reds"
)
st.plotly_chart(fig6, use_container_width=True)

# GRÁFICO 10: Top Atores Mais Frequentes 
top_atores = df_filtrado["ATORES"].str.split(",").explode().str.strip().value_counts().head(10).reset_index()
top_atores.columns = ["ATOR", "FILMES"]

fig_top_atores = px.bar(
    top_atores,
    x="FILMES",
    y="ATOR",
    orientation="h",
    title="🧑‍🎤 Top 10 Atores Mais Frequentes",
    color="FILMES",
    color_continuous_scale="Teal"
)
st.plotly_chart(fig_top_atores, use_container_width=True)

# GRÁFICO 11: Top 15 Piores Bilheterias
piores_bilheterias = df_filtrado.nsmallest(15, "BILHETERIA (MILHÕES $)")
fig7 = px.bar(
    piores_bilheterias,
    x="TÍTULO",
    y="BILHETERIA (MILHÕES $)",
    title="💸 Top 15 Piores Bilheterias (US$ Mi)",
    color="BILHETERIA (MILHÕES $)",
    color_continuous_scale="Pinkyl"
)
st.plotly_chart(fig7, use_container_width=True)

# GRÁFICO 12: Top 15 Piores Metascores
piores_metascores = df_filtrado.nsmallest(15, "METASCORE")
fig8 = px.bar(
    piores_metascores,
    x="TÍTULO",
    y="METASCORE",
    title="👎 Top 15 Piores Metascores",
    color="METASCORE",
    color_continuous_scale="Magenta"
)
st.plotly_chart(fig8, use_container_width=True)

# RODAPÉ 
st.markdown("---")
st.caption("Dados: IMDB • Dashboard desenvolvido por William Bruno com Streamlit 🚀")