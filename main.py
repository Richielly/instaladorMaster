from venvinstaladorMaster import search
import streamlit as st
from venvinstaladorMaster import api
from time import sleep as sl
import pandas as pd


# user = "conta@equiplano.com.br"
# senha = "EqpAlmoxarifado1974!@#"

user = "teste"
senha = "1"

st.set_page_config(page_title='Conversão Almox', page_icon='equiplano-logo-vertical.png', layout = 'wide', initial_sidebar_state = 'auto')

x,y = api.search_bd()
col1, col2, col3, col4, col5 = st.columns(5)

ambiente = st.sidebar.radio("Api",('Produção','Teste'))

postgre = st.sidebar.checkbox('Analise Banco Postgre')
firebird = st.sidebar.checkbox('Analise Banco FireBird')

if postgre:
    result = search.Search()
    tables = result.select_tables_postgre()
    tables_list = []
    for tab in tables:
        tables_list.append(tab[0])
    select_table = st.selectbox('Tabelas',tables_list)

    result2 = search.Search()
    columns = result2.select_columns_tables(select_table)
    columns_list = ['*', 'count(*)']
    for column in columns:
        columns_list.append(column[0])
    select_column = st.selectbox('colunas', columns_list)

    result3 = search.Search()
    find = result3.select_filter(select_table, select_column)

    st.write(pd.DataFrame(find))

if firebird:
    result_f = search.Search()
    tables_f = result_f.select_tables_firebird()
    tables_list_f = []
    for tab in tables_f:
        tables_list_f.append(tab[0])
    select_table_f = st.selectbox('Tabelas',tables_list_f)

    result_f2 = search.Search()
    columns_f = result_f2.select_columns_firebird(select_table_f)
    print(columns_f)
    columns_list_f = ['*', 'count(*)']
    for column_f in columns_f:
        columns_list_f.append(column_f[0])
    select_column_f = st.selectbox('Colunas', columns_list_f)

    result_f3 = search.Search()
    find_f3 = result_f3.select_filter_firebird(select_table_f, select_column_f)

    st.write(pd.DataFrame(find_f3))

if ambiente == 'Teste':
    user = "teste"
    senha = "1"
    url = "localhost:7575/almoxarifadoBackend/integracao/movimentos/estatistica/"
    chave = st.sidebar.text_input("Chave")
    if chave == "":
        result4 = search.Search()
        chave = result4.select_filter('configuracao', 'chaveacesso')
        chave = chave[[0][0]][0]
    tempo = st.sidebar.number_input("Tempo de Verificação", min_value=0, max_value=10, value=2, step=1)

if ambiente == 'Produção':
    user = "conta@equiplano.com.br"
    senha = "EqpAlmoxarifado1974!@#"
    url = st.sidebar.text_input("Url",'sistemaweb.candoi.pr.gov.br:7575/almoxarifadoBackend/integracao/movimentos/estatistica/')
    if url == "":
       st.error('Favor informar a Url do end point')
    chave = st.sidebar.text_input("Chave",'a643e6c8-71b6-4fd8-9313-0d4051afef19')
    if chave == "":
        st.error('Favor informar a chave de acesso do end point')
    tempo = st.sidebar.number_input("Tempo de Verificação", min_value=0, max_value=10, value=10, step=1)

if st.sidebar.button("Pré Analise"):
    st.empty()
    with st.empty():
        almox = api.buscar_dados(user=user, password=senha, url=url, chave=chave, tempo=tempo, x_bd=x, y_bd=y)

        form = st.form("form_analise", clear_on_submit=True)

        with col1:
            st.metric(almox[1]['x'][0], almox[0]['y'][0], int(almox[1]['y'][0]) - int( almox[0]['y'][0]))
            st.metric(almox[1]['x'][1], almox[0]['y'][1], int(almox[1]['y'][1]) - int( almox[0]['y'][1]))
            st.metric(almox[1]['x'][2], almox[0]['y'][2], int(almox[1]['y'][2]) - int( almox[0]['y'][2]))
            st.metric(almox[1]['x'][3], almox[0]['y'][3], int(almox[1]['y'][3]) - int( almox[0]['y'][3]))

        with col2:
            st.metric(almox[1]['x'][4], almox[0]['y'][4], int(almox[1]['y'][4]) - int( almox[0]['y'][4]))
            st.metric(almox[1]['x'][5], almox[0]['y'][5], int(almox[1]['y'][5]) - int( almox[0]['y'][5]))
            st.metric(almox[1]['x'][6], almox[0]['y'][6], int(almox[1]['y'][6]) - int( almox[0]['y'][6]))
            st.metric(almox[1]['x'][7], almox[0]['y'][7], int(almox[1]['y'][7]) - int( almox[0]['y'][7]))

        with col3:
            st.metric(almox[1]['x'][8], almox[0]['y'][8], int(almox[1]['y'][8]) - int( almox[0]['y'][8]))
            st.metric(almox[1]['x'][9], almox[0]['y'][9], int(almox[1]['y'][9]) - int( almox[0]['y'][9]))
            st.metric(almox[1]['x'][10], almox[0]['y'][10], int(almox[1]['y'][10]) - int( almox[0]['y'][10]))
            st.metric(almox[1]['x'][11], almox[0]['y'][11], int(almox[1]['y'][11]) - int( almox[0]['y'][11]))

        with col4:
            st.metric(almox[1]['x'][12], almox[0]['y'][12], int(almox[1]['y'][12]) - int( almox[0]['y'][12]))
            st.metric(almox[1]['x'][13], almox[0]['y'][13], int(almox[1]['y'][13]) - int( almox[0]['y'][13]))
            st.metric(almox[1]['x'][14], almox[0]['y'][14], int(almox[1]['y'][14]) - int( almox[0]['y'][14]))
            st.metric(almox[1]['x'][15], almox[0]['y'][15], int(almox[1]['y'][15]) - int( almox[0]['y'][15]))


if st.sidebar.button("Gráfico"):
    st.empty()
    with st.empty():
        grafico = api.buscar_dados(user=user, password=senha, url=url, chave=chave, tempo=tempo, x_bd=x, y_bd=y)
        st.plotly_chart(grafico,sharing='streamlit',use_container_width=True)

if st.sidebar.button("Verificação tempo real"):
    st.empty()
    with st.empty():
        while (True):
            grafico = api.buscar_dados(user=user, password=senha, url=url, chave=chave, tempo=tempo, x_bd=x, y_bd=y)
            st.plotly_chart(grafico,sharing='streamlit',use_container_width=True)
            sl(tempo)
