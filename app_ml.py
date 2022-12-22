import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

def run_ml_app() :
    df = pd.read_csv('data/realeditdrama.csv', thousands = ',')
    df_main = df.loc[:,['drama_name','Content Rating','score','Popularity','Episodes','platforms']]
    

    select_rank = st.sidebar.selectbox('항목별 ', ['전체','장르별','태그별','배우별'])
    status = st.radio('드라마랭킹 top100',['인기순','평점순','리뷰순'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if select_rank =='전체' :
        
        if status == '인기순' :
            st.dataframe(df.loc[:,['drama_name','Popularity']].sort_values('Popularity').head(100))
                
        elif status == '평점순' :
            st.dataframe(df.loc[:,['drama_name','score']].sort_values('score',ascending=False).head(100) )
        elif status == '리뷰순' :
            st.dataframe(df.loc[:,['drama_name','scored by']].sort_values('scored by',ascending=False ).head(100))
        elif status == '조회순' :
            st.dataframe(df.loc[:,['drama_name','Watchers']].sort_values('Watchers',ascending=False).head(100) )


    if select_rank =='장르별' :
        genre_scpore = pd.read_csv('data/genre_scpore.csv',index_col='genre')
        genre_sum = pd.read_csv('data/genre_sum.csv')
        st.dataframe(genre_scpore)

        if status == '인기순':
           
            st.subheader('화제를 모으는 작품이 많은 장르순입니다')
            st.dataframe(genre_scpore.loc[:,['popul']].sort_values('popul'))
            list = genre_scpore.sort_values('popul').head(10)
            select = st.selectbox('화제를 모으는 작품이 많은 장르별 드라마',list )
            st.dataframe(df_main[df['Genres'].str.contains(str(select),na=False)],)
            

        if status == '평점순':    
            st.subheader('평가가 좋은 작품이 많은 장르입니다')
            st.dataframe(genre_scpore.loc[:,['score']].sort_values('score',ascending=False))
            list = genre_scpore.sort_values('score',ascending=False).head(10)
            select = st.selectbox('평가가 좋은 드라마가 많은 장르별 드라마',list )
            st.dataframe(df_main[df['Genres'].str.contains(str(select),na=False)])


        if status == '리뷰순':
            st.subheader('시청자 작품 장르입니다')
            st.dataframe(genre_scpore.loc[:,['review']].sort_values('review',ascending=False))
            list = genre_scpore.sort_values('review',ascending=False).head(10)
            select = st.selectbox('리뷰가 많이 달린 드라마 장르 목록',list )
            st.dataframe(df_main[df['Genres'].str.contains(str(select),na=False)])
        
        
        
    if select_rank =='태그별' :
        tag_slporesum = pd.read_csv('data/tag_slporesum.csv',index_col='tag')
        st.dataframe(tag_slporesum)
        
      

        if status == '인기순' :
            st.subheader('인기가 많은 드라마 진행 방식입니다')
            st.dataframe(tag_slporesum[tag_slporesum['sum'] >10].loc[:,['Popularity']].sort_values('Popularity'))
            list = tag_slporesum[tag_slporesum['sum'] >10].sort_values('Popularity').head(10)
            select = st.selectbox('인기 태그별 대표 드라마 목록 입니다',list )
            st.dataframe(df_main[df['Tags'].str.contains(str(select),na=False)],)


        if status == '평점순':
            st.subheader('평가가 좋은 작품이 많은 장르입니다')
            st.dataframe(tag_slporesum[tag_slporesum['sum'] >10].loc[:,['score']].sort_values('score',ascending=False))
            list = tag_slporesum[tag_slporesum['sum'] >10].sort_values('score').head(10)
            select = st.selectbox('태그별 평가가 좋은 대표 드라마 목록 입니다',list )
            st.dataframe(df_main[df['Tags'].str.contains(str(select),na=False)],)


        if status == '리뷰순':
            st.subheader('리뷰가 많이 달리는 태그별 작품입니다')
            st.dataframe(tag_slporesum[tag_slporesum['sum'] >10].loc[:,['review']].sort_values('review',ascending=False))
            list = tag_slporesum[tag_slporesum['sum'] >10].sort_values('review').head(10)
            select = st.selectbox('태그별 평가가 좋은 대표 드라마 목록 입니다',list )
            st.dataframe(df_main[df['Tags'].str.contains(str(select),na=False)],)


    if select_rank =='배우별' :
        pass
