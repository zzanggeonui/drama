import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
translator = Translator()
st.set_page_config(layout="wide")
df_name = pd.read_csv('data/drama_name.csv')

def run_home_app() :
    status = st.radio('드라마랭킹 top100',['인기순','평점순','리뷰순','시청순'])
    df= pd.read_csv('data/realeditdrama.csv')

    if status == '인기순' :
        st.dataframe(df.loc[:,['drama_name','Popularity']].sort_values('Popularity').head(100))
    elif status == '평점순' :
        st.dataframe(df.loc[:,['drama_name','score']].sort_values('score',ascending=False).head(100) )
    elif status == '리뷰순' :
        st.dataframe(df.loc[:,['drama_name','scored by']].sort_values('scored by',ascending=False ).head(100))
    elif status == '시청순' :
        st.dataframe(df.loc[:,['drama_name','Watchers']].sort_values('Watchers').head(100) )

    select = st.text_input('드라마 제목을 입력하세요')
    if len(select) != 0 :
        serch = 'https://mydramalist.com/search?q='+select
        re = requests.get(serch)
        ra = re.text
        htm = BeautifulSoup(ra, 'html.parser')
        href = htm.find('div').find('h6').find('a')['href']
        link = 'https://mydramalist.com'+href
        req = requests.get(link)
        raw = req.text
        html = BeautifulSoup(raw, 'html.parser')
        infos = html.select('div.show-synopsis')
        
        name_select = st.selectbox('드라마확인',df_name[df_name['name'].str.contains(str('Youth'),na=False)])

        url = html.select_one('#content > div > div.container-fluid.title-container > div > div.col-lg-8.col-md-8.col-rightx > div:nth-child(1) > div.box-body > div > div.col-sm-4.film-cover.cover > a.block > img')['src']
        st.image(url)
        st.subheader('시놉시스')
        for title in infos :
            synop = title.get_text()
            st.markdown(synop)
            see_list = ['drama_name','Ranked','Popularity','score','Content Rating','actors','Episodes','platforms']	
            st.dataframe(df.loc[df['drama_name'].str.contains(select),see_list])
    
        
