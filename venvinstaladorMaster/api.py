import json, requests
from requests.auth import HTTPBasicAuth
import streamlit as st
from time import sleep as sl
import plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go
from search import Search
import pandas as pd

# localhost:7575/almoxarifadoBackend/integracao/movimentos/estatistica/e58c5576-311c-4c0f-9222-6b9fd830515d
select = Search()

@st.cache
def load_data(nrows):
    data = pd.read_csv('train.csv', nrows=nrows)
    return data

def search_bd():
    in_banco = select.select()

    lista_x_banco = []
    lista_y_banco = []
    lista_paginas = []
    for j in in_banco:
        lista_x_banco.append(j[0])  # tabela
        lista_y_banco.append(j[1])  # quantidade de dados
        # lista_paginas.append(j[2]) #paginas
    return lista_x_banco, lista_y_banco

def buscar_dados(user, password, url, chave, tempo,x_bd, y_bd):
    # print(requests.get('http://localhost:7575/almoxarifado', auth=HTTPBasicAuth(user, password)))

    # request = requests.get("http://realezapr.equiplano.com.br:8080/almoxarifadoBackend/integracao/movimentos/estatistica/c8a815d5-3e71-45c7-b03f-06376d57cfd8")

    request = requests.get('http://' + url + chave)

    # print(request.status_code)

    todos = json.loads(request.content)
    # print(todos)

    lista_tabela_x=[]
    lista_tabela_y = []

    todos.pop(13) # Excluindo tabela solicitação
    for i in todos:
        lista_tabela_x.append(i['tabela'])
        lista_tabela_y.append(i['totalAlmoxarifado'])

    banco = lista_tabela_x

    almox = lista_tabela_x

    data = [banco, almox]

    return data

# def grafico(dados):
#     st.plotly_chart(dados)

