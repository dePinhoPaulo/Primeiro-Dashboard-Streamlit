import streamlit as st
import pandas as pd

# Dados
df_copas = pd.read_csv('WorldCups.csv')
print(df_copas)

# Pagina: Edições
st.set_page_config(page_title="Edições", page_icon="🏆")
#st.sidebar.header("Edições")

# Painel
st.title('Análise das Ediçoes')
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

st.text('')

# Filtro com SelectBox
paises_disponiveis = df_copas['Country'].unique()
paises_selecionados = st.multiselect(
    'Selecione o Pais sede: ', 
    paises_disponiveis,
    default=paises_disponiveis
)

# Dataframe filtrado
df_copas_filtrado = df_copas[df_copas['Country'].isin(paises_selecionados)]


st.write(f'Análise de Gols por Paises: {paises_selecionados}')
st.bar_chart(
    data=df_copas_filtrado,
    x='Year',
    y='GoalsScored'
)