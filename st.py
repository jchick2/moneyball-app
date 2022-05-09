import streamlit as st
import pandas as pd
import requests 
from bs4 import BeautifulSoup

tag = st.selectbox('choose a topic', ['players', 'hitting'])

url = f"https://www.baseball-reference.com/teams/ATL/2022.shtml#team_batting/{tag}/"

res = requests.get(url)

content = BeautifulSoup(res.content, 'html.parser' )

quotes = content.find_all('div', class_='quotes')

for quote in quotes: 
    text = quote.find('span', class_='text')
    author = quote.find('small', class_='author')
    link = quote.find('a')
    st.success(text)
    st.write(author)
    st.code(link)

    df = pd.DataFrame(
        np.random.randn(10,5),
        columns=('col %d' % i for i in range(5)))

    st.table(df)
    
    