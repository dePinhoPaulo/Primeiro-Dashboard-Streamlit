import streamlit as st
import pandas as pd

# Dados
df_edicoes = pd.read_csv('wc_all_editions.csv')

todos_paises = pd.concat([
    df_edicoes['champion'], 
    df_edicoes['runner_up'], 
    df_edicoes['third_place'], 
    df_edicoes['fourth_place']
]).unique()

# Ordenar a lista em ordem alfabética
todos_paises = sorted(todos_paises)

# Pagina: Edições
st.set_page_config(page_title="Histórico", page_icon="📉")
#st.sidebar.header("Edições")

# Painel
st.title("Desempenho Histórico por País")

# Filtro de seleção
pais_selecionado = st.selectbox("Selecione um País:", todos_paises)

# Guardar a trajetória do país selecionado
trajetoria = []

# Varremos linha por linha da planilha original para descobrir a posição do país em cada ano
for index, linha in df_edicoes.iterrows():
    ano = linha['year']
    
    if linha['champion'] == pais_selecionado:
        trajetoria.append({'Ano': ano, 'Colocacao': 1})
    elif linha['runner_up'] == pais_selecionado:
        trajetoria.append({'Ano': ano, 'Colocacao': 2})
    elif linha['third_place'] == pais_selecionado:
        trajetoria.append({'Ano': ano, 'Colocacao': 3})
    elif linha['fourth_place'] == pais_selecionado:
        trajetoria.append({'Ano': ano, 'Colocacao': 4})

df_trajetoria = pd.DataFrame(trajetoria)

# Se o país já terminou no Top 4 alguma vez, mostramos o gráfico
if not df_trajetoria.empty:
    df_grafico = df_trajetoria.set_index('Ano')
    
    st.line_chart(df_grafico['Colocacao'])
    
    st.write("Tabela de dados do gráfico:")
    st.dataframe(df_trajetoria)

else:
    st.warning("Este país nunca terminou entre os 4 primeiros colocados.")