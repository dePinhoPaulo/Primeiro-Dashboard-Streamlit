import streamlit as st
import pandas as pd

# Dados
df_copas = pd.read_csv('WorldCups.csv')
print(df_copas)

# Pagina: Edições
st.set_page_config(page_title="Histórico", page_icon="📉")
#st.sidebar.header("Edições")

# Painel
st.title('Histórico de Seleções & Desempenho')
st.write('Filtre as seleções que deseja analisar:')

st.text('')