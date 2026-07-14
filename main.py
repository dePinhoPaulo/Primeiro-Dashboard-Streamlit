import streamlit as st
import pandas as pd

# Pagina: Edições
st.set_page_config(page_title="Copas do Mundo", page_icon="🏆")
#st.sidebar.header("Edições")

# Sistema de Login simples
if 'logado' not in st.session_state:
    st.session_state['logado'] = False

if not st.session_state['logado']:
    st.title('🔑 Login do Sistema')

    with st.form('formulario_login'):
        usuario = st.text_input('Usuário')
        senha = st.text_input('Senha', type='password')
        botao_entrar = st.form_submit_button('Entrar')

    if botao_entrar:
        if usuario == 'admin' and senha == '1234':
            st.session_state['logado'] = True
            st.success('Login realizado com sucesso!')
            st.rerun()
        else:
            st.error('Usuário ou senha incorreta!')

else:
    if st.sidebar.button('🔓 Sair / Logout'):
        st.session_state['logado'] = False
        st.rerun()

    # Painel
    home = st.Page('home.py', title='Home', icon='🏚', default=True)
    edicoes = st.Page('pagina_edicoes.py', title='Edições', icon='🏆')
    jogadores = st.Page('pagina_jogadores.py', title='Jogadores', icon='⚽')

    navegacao = st.navigation([home, edicoes, jogadores])
    navegacao.run()
