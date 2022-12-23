import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px


## 한글 나옴
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')



def run_eda_app() :
    df = pd.read_csv('data/realeditdrama.csv', thousands = ',')
   

    
    
    st.subheader('●분류별 드라마 분석')
    pie_list = ['장르','태그','플랫폼']
    use_select = st.selectbox('',pie_list)
    if use_select == '태그' :
        tag = df['Tags']
        tag_list = []
        for x in tag :
            x = x.split(',')
            for x2 in x :
                x2 = x2.strip(" ")
                x2 = x2.strip("''")
                tag_list.append(x2)
        tag_sum = pd.DataFrame(pd.DataFrame(data=tag_list).rename(columns={0:'tag'}).value_counts()).rename(columns={0:'sum'}).reset_index()
        fig3 = px.pie(tag_sum.head(10), 'tag','sum',title='한국 드라마에서 가장많이 사용된 진행 형식은? ')
        st.plotly_chart(fig3)

        fig4 = px.bar(tag_sum, x='tag', y='sum')
        st.plotly_chart(fig4)
        if st.button('전체 태그별 작품수 확인') :
            st.dataframe(tag_sum)

    if use_select == '장르' :
        genre_sum = pd.read_csv('data/genre_sum.csv').drop('gneres',axis=1)

        fig = px.pie(genre_sum.head(10), 'genre','sum',title='드라마로 많이 제작되는 장르는?? ')
        st.plotly_chart(fig)

        fig2 = px.bar(genre_sum.head(15), x='genre', y='sum')
        st.plotly_chart(fig2)
        if st.button('전체 장르별 작품수 확인') :
            st.dataframe(genre_sum)


    if use_select == '플랫폼' :
        platforms = df['platforms']
        platforms_list = []
        for x in platforms :
            x = x.split(',')
            for x2 in x :
                x2 = x2.strip(" ")
                x2 = x2.strip("''")
                platforms_list.append(x2)
        plat = pd.DataFrame(pd.DataFrame(data =platforms_list).value_counts()).rename(columns={0:'sum'}).reset_index().rename(columns={0:'platforms'})
        fig3 = px.pie(plat.head(10), 'platforms','sum',title='가장 많은 드라마를 볼수 있는 플랫폼은? ')
    
        st.plotly_chart(fig3)

        fig4 = px.bar(plat.head(15), x='platforms', y='sum')
        st.plotly_chart(fig4)
        if st.button('전체 플랫폼별 볼수있는 작품수 확인') :
            st.dataframe(plat)
    
    
    st.subheader('●히스토그램 분석')
    columns = ['점수','러닝타임','에피소드수','연령제한']
    df_hist = df.loc[:,['score','Duration','Episodes','Content Rating']]
    df_hist.columns = ['점수','러닝타임','에피소드수','연령제한']
    histogram_column = st.selectbox('',columns)
    my_bins = st.number_input('빈의 갯수를 입력하세요', 25, 50, value=30, step=1)
    
    if histogram_column == '연령제한':
        st.info(' 한국드라마의 {} 분포확인 '.format(histogram_column))
        fig1 = plt.figure()
        plt.hist(data= df_hist, x=histogram_column, rwidth=0.8, bins=my_bins)
        plt.title(histogram_column + ' Histogram')
        plt.xlabel(histogram_column)
        plt.xticks(rotation = 45)
        plt.ylabel('Count')
        st.pyplot(fig1)
        if st.button('describe 보기') :
            st.dataframe(df.hist['연령제한'].value_counts())


    else :
        st.info(' 한국드라마의 {} 분포 확인 '.format(histogram_column))
        fig1 = plt.figure()
        plt.hist(data= df_hist, x=histogram_column, rwidth=0.8, bins=my_bins)
        plt.title(histogram_column + ' Histogram')
        plt.xlabel(histogram_column)
        plt.ylabel('Count')
        st.pyplot(fig1)
        st.write(df_hist[histogram_column].describe())



    st.subheader('●드라마 상관관계 분석')
    selected_list = st.multiselect('원하는 컬럼을 선택해주세요',columns)
    if len(selected_list) >= 2 :
            df_corr = df.loc[:,['Episodes','Duration','score','Watchers','scored by','Ranked','Popularity']]
            df_corr.columns = ['에피소드수', '러닝타임' ,'점수','사이트 조회수' ,'리뷰수' ,'순위' ,'화제성']
            df_corr = df_corr[selected_list].corr()

            df_corr

            fig2 = plt.figure()
            sb.heatmap(data= df_corr, annot=True, fmt='.2f', cmap='coolwarm',
                vmin= -1, vmax= 1 , linewidths=0.5 )
            st.pyplot(fig2)
            st.info('화제성 과 순위는 낮은 숫자일수록 좋은 지수로, 반비례 할때 관계성이 좋은 지표입니다')



