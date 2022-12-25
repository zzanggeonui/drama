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
    df_main = df.loc[:,['drama_name','Content Rating','scored by','score','Popularity','Episodes','actors','Genres','Tags','platforms']]
    df_main.columns  = ['작품명','연령제한','리뷰수','점수별','인기별','에피소드수','배우', '장르','태그','플랫폼' ]
    genre_scporesum = pd.read_csv('data/genre_scporesum.csv').drop('genre',axis=1)
    tag_slporesum = pd.read_csv('data/tag_slporesum.csv').drop('tags',axis=1)
    actor_slporesum = pd.read_csv('data/actor_slporesum.csv').drop('actors',axis=1)
    platforms_slporesum = pd.read_csv('data/platforms_slporesum.csv').drop('index',axis=1)

    st.subheader('●분류별 드라마 분석')
    user_select1 = st.selectbox('',['장르','태그','플랫폼','배우'])
    user_select2 = st.selectbox('',['점수별','인기별','리뷰수','작품수'])
    st.write('<style>div.row-widget.stSelectbox > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    st.subheader('전체 {} , 상위 {} 확인'.format(user_select1,user_select2))

    if user_select1 == '장르' :
        if user_select2 == '인기별' :
            list = genre_scporesum.sort_values(user_select2)
            st.dataframe(list)
        else :
            list = genre_scporesum.sort_values(user_select2,ascending=False)
            st.dataframe(list)
    if user_select1 == '태그' :
        if user_select2 == '인기별' :
            list = tag_slporesum[tag_slporesum['작품수'] >10].sort_values(user_select2)
            st.dataframe(list)
            
        else :
            list = tag_slporesum[tag_slporesum['작품수'] >10].sort_values(user_select2,ascending=False)
            st.dataframe(list)
    if user_select1 == '플랫폼' :
        if user_select2 == '인기별' :
            list = platforms_slporesum[platforms_slporesum['작품수'] >5].sort_values(user_select2)
            st.dataframe(list)
        else :
            list = platforms_slporesum[platforms_slporesum['작품수'] >5].sort_values(user_select2,ascending=False)
            st.dataframe(list)
    if user_select1 == '배우' :
        if user_select2 == '인기별' :
            list = actor_slporesum[actor_slporesum['작품수'] >5].sort_values(user_select2)
            st.dataframe(list)
        else :
            list = actor_slporesum[actor_slporesum['작품수'] >5].sort_values(user_select2,ascending=False)
            st.dataframe(list)

    st.subheader('{}순, {} 대표작품'.format(user_select2,user_select1))
    select = st.selectbox('',list )
    st.dataframe(df_main[df_main[user_select1].str.contains(str(select),na=False)],)
    

    if user_select1 == '태그' :
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

        fig4 = px.bar(tag_sum.head(15), x='tag', y='sum')
        st.plotly_chart(fig4)

        


    if user_select1 == '장르' :
        genre = df['Genres'].dropna()
        genre_list = []
        for x in genre :
            x = x.split(',')
            for x2 in x :
                x2 = x2.strip(" ")
                x2 = x2.strip("''")
                genre_list.append(x2)
        genre_sum = pd.DataFrame(pd.DataFrame(data=genre_list).rename(columns={0:'genre'}).value_counts()).rename(columns={0:'sum'}).reset_index()

        fig = px.pie(genre_sum.head(10), 'genre','sum',title='드라마로 많이 제작되는 장르는?? ')
        st.plotly_chart(fig)

        fig2 = px.bar(genre_sum.head(15), x='genre', y='sum')
        st.plotly_chart(fig2)
    
    

    if user_select1 == '플랫폼' :
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
    df_hist = df.loc[:,['score','Duration','Episodes','Content Rating']].dropna()
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
        
        st.write(df_hist['연령제한'].value_counts())
           

    else :
        st.info(' 한국드라마의 {} 분포 확인 '.format(histogram_column))
        fig1 = plt.figure()
        plt.hist(data= df_hist, x=histogram_column, rwidth=0.8, bins=my_bins)
        plt.title(histogram_column + ' Histogram')
        plt.xlabel(histogram_column)
        plt.ylabel('Count')
        st.pyplot(fig1)
        st.write('{}에 평균은 {} 입니다'.format(histogram_column,df_hist[histogram_column].mean()))
        st.write('{}에 최소값은 {} 입니다'.format(histogram_column,df_hist[histogram_column].min()))
        st.write('{}에 최대값은 {} 입니다'.format(histogram_column,df_hist[histogram_column].max()))

  

    st.subheader('●드라마 상관관계 분석')
    selected_list = st.multiselect('원하는 컬럼을 선택해주세요',['에피소드수', '러닝타임' ,'점수','사이트 조회수' ,'리뷰수' ,'순위' ,'화제성','연령제한'])
    if len(selected_list) >= 2 :
            df_corr = df.loc[:,['Episodes','Duration','score','Watchers','scored by','Ranked','Popularity','Content Rating']]
            df_corr.columns = ['에피소드수', '러닝타임' ,'점수','사이트 조회수' ,'리뷰수' ,'순위' ,'화제성','연령제한']
            df_corr = df_corr[selected_list].corr()

         

            fig2 = plt.figure()
            sb.heatmap(data= df_corr, annot=True, fmt='.2f', cmap='coolwarm',
                vmin= -1, vmax= 1 , linewidths=0.5 )
            st.pyplot(fig2)
            st.dataframe(df_corr)
            st.info('화제성 과 순위는 낮은 숫자일수록 좋은 지수로, 반비례 할때 관계성이 좋은 지표입니다')



