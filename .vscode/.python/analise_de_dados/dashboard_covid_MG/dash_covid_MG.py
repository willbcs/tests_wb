import streamlit as st
import pandas as pd
import plotly.express as px

# ======================== CONFIG PÁGINA ========================
st.set_page_config(
    page_title="Óbitos COVID-19 MG",
    layout="wide",
    page_icon="🦠"
)

st.title("🦠 Painel de Óbitos Confirmados por COVID-19 - Minas Gerais")

# ======================== CARREGAR DADOS ========================
@st.cache_data
def carregar_dados():
    df = pd.read_csv(
        'OBITOS_CONF_COVID-19_MG.csv',
        sep=";", encoding="latin1"
    )
    df = df.drop(columns=[col for col in df.columns if "Unnamed" in col])
    df.columns = df.columns.str.strip().str.upper().str.replace(" ", "_")
    df["DATA_DO_ÓBITO"] = pd.to_datetime(df["DATA_DO_ÓBITO"], format="%d/%m/%Y", errors='coerce')
    return df

df = carregar_dados()

# ======================== PRÉ-PROCESSAMENTO ========================
df["MUNICÍPIO_DE_RESIDÊNCIA"] = df["MUNICÍPIO_DE_RESIDÊNCIA"].str.strip()
df["COMORBIDADE"] = df["COMORBIDADE"].str.strip().str.upper()
df["SEXO"] = df["SEXO"].str.upper().replace({"M": "MASCULINO", "F": "FEMININO"})

# ======================== FILTRO DE CIDADE ========================
cidades = ["TODOS"] + sorted(df["MUNICÍPIO_DE_RESIDÊNCIA"].unique())
cidade_selecionada = st.sidebar.selectbox("Selecione a cidade", cidades)

if cidade_selecionada != "TODOS":
    df_filtro = df[df["MUNICÍPIO_DE_RESIDÊNCIA"] == cidade_selecionada]
else:
    df_filtro = df

# ======================== COLUNAS DE GRÁFICOS ========================
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# GRÁFICO 1 - Pizza Sexo (apenas percentual no centro)
sexo_count = df_filtro["SEXO"].value_counts(normalize=True).reset_index()
sexo_count.columns = ["SEXO", "PERCENTUAL"]
sexo_count["PERCENTUAL"] *= 100

fig_sexo = px.pie(
    sexo_count,
    names="SEXO",
    values="PERCENTUAL",
    title="♂️♀️ Óbitos por sexo",
    color_discrete_sequence=["#4C72B0", "#DD8452"]
)
fig_sexo.update_traces(
    textinfo='percent',
    textfont_color='white',
    texttemplate='%{percent:.1%}'  # Mostra 42.1%, 57.9% etc.
)
col1.plotly_chart(fig_sexo, use_container_width=True)

# GRÁFICO 2 - Pizza Comorbidades (com "NÃO INFORMADO" destacado e texto branco)
comorb = df_filtro["COMORBIDADE"].replace({"NÃO INFORMADO ": "NÃO INFORMADO", "NÃO ": "NÃO"})
comorb_count = comorb.value_counts(normalize=True).reset_index()
comorb_count.columns = ["COMORBIDADE", "PERCENTUAL"]
comorb_count["PERCENTUAL"] *= 100  # Converter para porcentagem

cores_comorbidades = ["#34495E", "#5D6D7E", "#85929E", "#AEB6BF"]

fig_comorb = px.pie(
    comorb_count,
    names="COMORBIDADE",
    values="PERCENTUAL",
    title="🏥 Óbitos por comorbidade",
    color_discrete_sequence=cores_comorbidades
)
fig_comorb.update_traces(
    textinfo='percent',
    textfont_color='white',
    texttemplate='%{percent:.1%}',  # Formato do percentual
    
)
col2.plotly_chart(fig_comorb, use_container_width=True)

# GRÁFICO 3 - Histograma Idade
fig_idade = px.histogram(
    df_filtro,
    x="IDADE",
    nbins=30,
    title="📊 Distribuição de idade dos óbitos",
    color_discrete_sequence=["#722F37"],
    labels={"count": "Quantidade", "IDADE": "IDADE"}  # Opcional: rótulo do eixo X
)

fig_idade.update_layout(yaxis_title="ÓBITOS")

col3.plotly_chart(fig_idade, use_container_width=True)

# GRÁFICO 4 - Óbitos por faixa etária
bins = [0, 18, 30, 45, 60, 75, 90, 200]
labels = ["0-17", "18-29", "30-44", "45-59", "60-74", "75-89", "90+"]
df_filtro["FAIXA_ETARIA"] = pd.cut(df_filtro["IDADE"], bins=bins, labels=labels, right=False)
faixa_count = df_filtro["FAIXA_ETARIA"].value_counts().sort_index().reset_index()
faixa_count.columns = ["FAIXA_ETARIA", "ÓBITOS"]
fig_faixa = px.bar(
    faixa_count,
    x="FAIXA_ETARIA",
    y="ÓBITOS",
    title="📏 Óbitos por faixa etária",
    color_discrete_sequence=["#1F497D"]  
)
col4.plotly_chart(fig_faixa, use_container_width=True)

# GRÁFICO 5 - Óbitos por mês 
df_filtro["ANO_MES"] = df_filtro["DATA_DO_ÓBITO"].dt.to_period("M").astype(str)
obitos_mes = df_filtro.groupby("ANO_MES").size().reset_index(name="ÓBITOS")
fig_mes = px.line(
    obitos_mes,
    x="ANO_MES",
    y="ÓBITOS",
    markers=True,
    title="📈 Óbitos confirmados por mês",
    color_discrete_sequence=["#E74C3C"]  
)
st.plotly_chart(fig_mes, use_container_width=True)

# GRÁFICO 6 - Top 15 cidades por média de idade dos óbitos 
media_idade = df.groupby("MUNICÍPIO_DE_RESIDÊNCIA")["IDADE"].mean().round(1).reset_index()
media_idade.columns = ["MUNICÍPIO", "IDADE"]
media_idade = media_idade.sort_values(by="IDADE", ascending=False).head(15)
fig_media_idade = px.bar(
    media_idade,
    x="IDADE",
    y="MUNICÍPIO",
    orientation="h",
    title="🧓 Top 15 cidades por média de idade dos óbitos",
    color="IDADE",
    color_continuous_scale="Blues"
)
fig_media_idade.update_layout(yaxis=dict(tickfont=dict(size=10)))
st.plotly_chart(fig_media_idade, use_container_width=True)

# ======================== GRÁFICO FINAL - TOP 15 CIDADES ========================
top_cidades = df["MUNICÍPIO_DE_RESIDÊNCIA"].value_counts().head(15).reset_index()
top_cidades.columns = ["MUNICÍPIO", "ÓBITOS"]
fig_top = px.bar(
    top_cidades,
    x="ÓBITOS",
    y="MUNICÍPIO",
    orientation="h",
    color="ÓBITOS",
    color_continuous_scale="Reds",
    title="🏙️ Top 15 cidades com mais óbitos confirmados por COVID-19"
)
st.plotly_chart(fig_top, use_container_width=True)

# ======================== RODAPÉ ========================
st.markdown("---")
st.caption("Fonte: SES/MG • Dashboard desenvolvido por William Bruno usando Streamlit 🚀")
