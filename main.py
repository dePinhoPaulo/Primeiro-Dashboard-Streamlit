import streamlit as st
import pandas as pd

# Pagina: Edições
st.set_page_config(page_title="Copas do Mundo", page_icon="🏆")
#st.sidebar.header("Edições")

# Painel
home = st.Page('home.py', title='Home', icon='🏚', default=True)
edicoes = st.Page('pagina_edicoes.py', title='Edições', icon='🏆')
jogadores = st.Page('pagina_jogadores.py', title='Jogadores', icon='⚽')

navegacao = st.navigation([home, edicoes, jogadores])
navegacao.run()

