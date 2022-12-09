import pandas as pd
import requests
import streamlit as st
from pandas import DataFrame


@st.cache
def load_data() -> DataFrame:
    url='https://www.fundsexplorer.com.br/ranking'
    html = requests.get(url)
    auxiliar_html=pd.read_html(html.text)
    return auxiliar_html[0]

st.set_page_config(layout='wide')

with st.sidebar:
    st.radio('Select one:', [1, 2])
    st.selectbox('Pick one', ['MXRF11'])
    st.button('Refresh')

st.metric('My metric', 42, 2)

st.title("Açoes")

data = load_data()

st.dataframe(data)
# st.download_button('Download file', data)
