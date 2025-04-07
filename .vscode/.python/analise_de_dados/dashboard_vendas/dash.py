# Faturamento por mês e por loja
# Faturamento por produto
# Faturamento por formas de pagamento
# Faturamento por loja

import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página...
st.set_page_config(
    page_title="Dashboard de Vendas",
    page_icon="📊",
    layout="wide"
)
df = pd.read_csv(r'C:\Users\Myrath\Desktop\Projetos_VSCode\.vscode\.python\analise_de_dados\dashboard_vendas\dados_vendas.csv', delimiter=';', encoding = "ISO-8859-1")

df["DATA_VENDA"] = pd.to_datetime(df["DATA_VENDA"])
df = df.sort_values("DATA_VENDA")

# Verificando quantos meses tem no DataFrame
df["MES"] = df["DATA_VENDA"].apply(lambda x: str(x.month) + "-" + str(x.year))

# Variável mês será inserido na Siderbar
mes = st.sidebar.selectbox("Mês", df["MES"].unique())

# Filtrando o mês
df_filtro = df[df["MES"] == mes]
df_filtro

# Criando as colunas do Dashboard
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

fig_date = px.bar(df_filtro, x = "DATA_VENDA", y = "VALOR_TOTAL", color = "LOJA", title = "Faturamento por dia")
col1.plotly_chart(fig_date)

fig_prod = px.bar(df_filtro, x = "VALOR_TOTAL", y = "PRODUTO", color = "LOJA", title = "Faturamento por produto", orientation="h")
col2.plotly_chart(fig_prod)

loja_total = df_filtro.groupby("LOJA")[["VALOR_TOTAL"]].sum().reset_index()
fig_loja = px.bar(loja_total, x = "LOJA", y = "VALOR_TOTAL", title="Faturamento por Loja")
col3.plotly_chart(fig_loja)

fig_pagto = px.pie(df_filtro, values = "VALOR_TOTAL", names = "FORMA_PAGAMENTO", title = "Faturamento por tipo de pagamento")
col4.plotly_chart(fig_pagto)

# ======================== RODAPÉ ========================
st.markdown("---")
st.caption("• Dashboard desenvolvido por William Bruno usando Streamlit 🚀")

#Abra a pasta do projeto e use o comando streamlit run dash.py no terminal para executar o dashboard.
