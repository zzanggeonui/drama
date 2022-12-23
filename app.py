import streamlit as st
import pandas as pd
from app_home import run_home_app
from app_eda import run_eda_app
from app_copy import run_sc_app
from googletrans import Translator
import requests
from bs4 import BeautifulSoup


def main() :
    st.set_page_config(layout="wide")
    df_name = pd.read_csv('data/drama_name.csv')
    df_actor = pd.read_csv('data/actor_list.csv')
    df_actor = df_actor.drop_duplicates()
    df= pd.read_csv('data/realeditdrama.csv', thousands = ',')
    translator = Translator()
    
    
    menu = ['홈','상세검색','분석']
    choice = st.sidebar.selectbox('메뉴',menu)
    
    radio_select = st.sidebar.radio('', ['드라마 제목','배우이름']) 
    st.sidebar.subheader('{}으로 검색'.format(radio_select))

    
    

    if radio_select == '드라마 제목' :


        select = st.sidebar.text_input('')
        if len(select) != 0 :
            name_select = st.sidebar.selectbox('드라마확인',df_name[df_name['name'].str.contains(str(select),na=False,case=False)])
            if str(name_select) in df_name['drama_name'].tolist() :
                serch = 'https://mydramalist.com/search?q='+name_select +'&adv=titles&ty=68&co=3&so=relevance'
                re = requests.get(serch)
                ra = re.text
                htm = BeautifulSoup(ra, 'html.parser')
                href = htm.find('div').find('h6').find('a')['href']
                link = 'https://mydramalist.com'+href
                req = requests.get(link)
                raw = req.text
                html = BeautifulSoup(raw, 'html.parser')
                infos = html.select('div.show-synopsis')
                
                

                url = html.select_one('#content > div > div.container-fluid.title-container > div > div.col-lg-8.col-md-8.col-rightx > div:nth-child(1) > div.box-body > div > div.col-sm-4.film-cover.cover > a.block > img')['src']
                st.sidebar.image(url)
                st.sidebar.subheader('시놉시스')
                for title in infos :
                    synop = title.get_text()
                    tr_result = translator.translate(synop,dest='ko').text
                    st.sidebar.markdown(tr_result)
                    see_list = ['drama_name','Ranked','Popularity','score','Content Rating','actors','Episodes','platforms']	
                    st.sidebar.dataframe(df.loc[df['drama_name'].str.contains(name_select),see_list])
            else :
                st.sidebar.text('검색결과가 없습니다')

    if radio_select == '배우이름' :    
        select = st.sidebar.text_input('')
        
        if len(select) != 0 :
            name_select = st.sidebar.selectbox('배우이름 확인',df_actor[df_actor['actor'].str.contains(str(select),na=False,case=False)])
            if str(name_select) in df_actor['actor'].tolist() :

                serch = 'https://mydramalist.com/search?q='+name_select
                re = requests.get(serch)
                ra = re.text
                htm = BeautifulSoup(ra, 'html.parser')
                href = htm.find('div').find('h6').find('a')['href']
                link = 'https://mydramalist.com'+href
                req = requests.get(link)
                raw = req.text
                html = BeautifulSoup(raw, 'html.parser')

                url = html.select_one('#content > div > div.container-fluid > div > div.col-lg-8.col-md-8 > div:nth-child(1) > div:nth-child(3) > div > div.col-sm-4.text-center.cover.hidden-md-up > img')['src']
                see_list = ['drama_name','Ranked','Popularity','score','Content Rating','actors','Episodes','platforms']
                st.sidebar.image(url)

                st.sidebar.subheader('대표작')
                most_drama = st.sidebar.dataframe(df.loc[df['actors'].str.contains(name_select, na= False ),see_list])
                
            else:
                st.sidebar.text('검색결과가 없습니다')



    if choice == '홈' :
        run_home_app()
        

    elif choice == '상세검색':
        run_sc_app()

    elif choice == '분석':
        run_eda_app()


if __name__ == '__main__':
    main()