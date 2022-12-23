import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
translator = Translator()
from PIL import Image

def run_home_app() :
    st.title('📺 K-Drama 데이터센터')
    url1 = 'https://kpophighindia.com/wp-content/uploads/2020/01/drama-cover.png'

    st.image(url1)
   
    with st.expander('데이터 프레임 소개') :
    
        df = pd.read_csv('data/realeditdrama.csv', thousands = ',',index_col='Unnamed: 0')
        
        df_main = df.loc[:,['drama_name','Genres','Tags','Content Rating','Duration','scored by','Watchers','score','Popularity','Episodes','actors','platforms']]
        st.dataframe(df_main)
        st.text('●Genres = 장르  \n●Tags= 태그 \n●Content Rating=시청등급  \n●Duration = 러닝타임 \n●scored by = 리뷰참여자수  \n●score = 평점  \n●Watchers = 사이트 조회수   \n●score = 점수 \n●Popularity = 인기도  \n●Episodes = 에피소드 숫자  \n●actors = 배우이름  \n●platforms = 현재 드라마를 볼 수있는 플랫폼')

    st.info('드라마 및 영상물 리뷰 전문 사이트인 IMDb와 MyDramaList의 한국 드라마 데이터를 기반으로 한국드라마 흥행요인 분석 및 검색 기능을 구현한 웹 대시보드 입니다. ')
    st.write('데이터 제공 :https://www.kaggle.com/datasets/iphigeniebera/korean-drama-list-about-740-unique-dramas')
    
