import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
translator = Translator()

def main() :


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
        st.subheader('시놉시스')
        for title in infos :
            synop = title.get_text()
            tr_results = translator.translate(synop,dest='ko')
            st.markdown(tr_results)
        url = html.select_one('#content > div > div.container-fluid.title-container > div > div.col-lg-8.col-md-8.col-rightx > div:nth-child(1) > div.box-body > div > div.col-sm-4.film-cover.cover > a.block > img')['src']
        st.image(url)
    

    df= pd.read_csv('data/editdrama.csv',index_col =0)
    df_genre= pd.read_csv('data/gentttttt.csv',index_col = 'genre')

    df_main = df.loc[:,['drama_name','actors','imdb_description','Genres']]
    selected_list = st.multiselect('장르를 선택하세요',df_genre )
    
    if len(selected_list) != 0 :

        st.dataframe(df[df['Genres'].str.contains(str('war'),na=False)])
        st.dataframe(df_main[df['Genres'].str.contains(str('war'),na=False)])
        

if __name__ == '__main__':
    main()