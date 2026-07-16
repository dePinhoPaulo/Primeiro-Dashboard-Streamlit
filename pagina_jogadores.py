import streamlit as st
import pandas as pd

# Dados
df_jogadores = pd.read_csv('wc_top_scorers.csv')
print(df_jogadores)

df_paises_artilheiros = (
    df_jogadores.groupby('country')['player']
    .count()
    .reset_index()
    .sort_values(by='player', ascending=False)
)

# Pagina: Edições
st.set_page_config(page_title="Jogadores", page_icon="⚽")
#st.sidebar.header("Edições")

# Painel
st.title('Análise dos Jogadores')
st.write('Maiores goleadores de Copas do Mundo:')

st.text('')

st.write('Atilheiros de cada edição: ')
st.bar_chart(
    data=df_jogadores,
    x='player',
    y='goals'
)

st.text('')

st.write('Tabela completa: ')
st.write(df_paises_artilheiros)

st.text('')

st.write('Pais com mais Atilheiros: ')
st.bar_chart(
    data=df_paises_artilheiros,
    x='country',
    y='player',
    horizontal=True
)