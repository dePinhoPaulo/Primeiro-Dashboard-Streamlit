import streamlit as st
import pandas as pd

# Dados
df_copas = pd.read_csv('WorldCups.csv')

print(df_copas)


# Painel
st.title('Meu primeiro Dashboard com Streamlit')
st.write('Edições de Copa do Mundo:')

st.text('')

st.write('Tabela completa: ')
st.write(df_copas)

st.text('')

st.write('Análise de Gols por edição: ')
st.line_chart(
    data=df_copas,
    x='Year',
    y='GoalsScored'
)