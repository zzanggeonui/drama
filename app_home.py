import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
translator = Translator()
from PIL import Image

def run_home_app() :
    st.title('🔥🔥K-DRAMA의 모든것🔥🔥')
    url = 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/korean-drama-series-1654114746.png?crop=0.502xw:1.00xh;0.250xw,0&resize=640:*'
    url1 = 'https://kpophighindia.com/wp-content/uploads/2020/01/drama-cover.png'

    st.image(url1)
   
    with st.expander('데이터 프레임 소개') :
    
        df = pd.read_csv('data/realeditdrama.csv', thousands = ',',index_col='Unnamed: 0')
        
        df_main = df.loc[:,['drama_name','Genres','Tags','Content Rating','Duration','scored by','Watchers','score','Popularity','Episodes','actors','platforms']]
        st.dataframe(df_main)
        st.text('Genres = 장르,  Tags= 태그,  Content Rating=시청등급,  Duration = 러닝타임,  scored by = 리뷰참여자수  \nscore = 평점,   Watchers = 사이트 조회수,   score = 점수  Popularity = 인기도  Episodes = 에피소드 숫자  \nactors = 배우이름,  platforms = 현재 드라마를 볼 수있는 플랫폼')

    st.info('드라마 및 영상물 리뷰 전문 사이트인 IMDb와 MyDramaList의 한국 드라마 데이터를 기반으로 한국드라마 흥행요인 분석 및 검색 기능을 구현한 웹 대시보드 입니다. ')
    
    
