import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt


def run_sc_app() :
    df = pd.read_csv('data/realeditdrama.csv', thousands = ',')
    df_main = df.loc[:,['drama_name','Content Rating','score','Popularity','Episodes','platforms']]
    
    st.title('항목별 상세 검색 페이지 입니다')
    select_rank = st.selectbox(' ', ['전체','장르별','태그별','배우별'])
    status = st.radio('드라마랭킹 top100',['인기순','평점순','화제순'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if select_rank =='전체' :
        
        if status == '인기순' :
            st.dataframe(df.loc[:,['drama_name','Popularity']].sort_values('Popularity').head(100))
                
        elif status == '평점순' :
            st.dataframe(df.loc[:,['drama_name','score']].sort_values('score',ascending=False).head(100) )
        elif status == '화제순' :
            st.dataframe(df.loc[:,['drama_name','scored by']].sort_values('scored by',ascending=False ).head(100))
        elif status == '조회순' :
            st.dataframe(df.loc[:,['drama_name','Watchers']].sort_values('Watchers',ascending=False).head(100) )


    if select_rank =='장르별' :
        genre_scpore = pd.read_csv('data/genre_scpore.csv',index_col='genre')
        genre_sum = pd.read_csv('data/gnre_sum.csv')

        if status == '인기순':
           
            st.subheader('시청자로부터 사랑을 받은 작품이 많은 장르순입니다')
            st.dataframe(genre_scpore.loc[:,['popul']].seort_values('popul'))
            list = genre_scpore.sort_values('popul').head(10)
            select = st.selectbox('인기가 많았던 장르별 드라마',list )
            st.dataframe(df_main[df['Genres'].str.contains(str(select),na=False)],)
            

        if status == '평점순':    
            st.subheader('평가가 좋은 작품이 많은 장르입니다')
            st.dataframe(genre_scpore.loc[:,['score']].sort_values('score',ascending=False))
            list = genre_scpore.sort_values('score',ascending=False).head(10)
            st.subheader('작품 평가가 좋은 장르별 드라마')
            select = st.selectbox('',list )
            st.dataframe(df_main[df['Genres'].str.contains(str(select),na=False)])


        if status == '화제순':
            st.subheader('화제가된 작품이 많은 장르입니다')
            st.dataframe(genre_scpore.loc[:,['review']].sort_values('review',ascending=False))
            list = genre_scpore.sort_values('review',ascending=False).head(10)
            st.subheader('화제가 된 장르별 드라마')
            select = st.selectbox('',list )
            st.dataframe(df_main[df['Genres'].str.contains(str(select),na=False)])
        
        
        
    if select_rank =='태그별' :
        tag_slporesum = pd.read_csv('data/tag_slporesum.csv',index_col='tags')
      
      

        if status == '인기순' :
            st.subheader('인기가 많은 드라마 태그입니다')
            st.dataframe(tag_slporesum[tag_slporesum['sum'] >10].loc[:,['Popularity']].sort_values('Popularity'))
            list = tag_slporesum[tag_slporesum['sum'] >10].sort_values('Popularity').head(10)
            st.subheader('인기 태그별 드라마 목록 입니다 입니다')
            select = st.selectbox('',list )
            st.dataframe(df_main[df['Tags'].str.contains(str(select),na=False)],)


        if status == '평점순':
            st.subheader('평가가 좋은 작품의 태그 입니다')
            st.dataframe(tag_slporesum[tag_slporesum['sum'] >10].loc[:,['score']].sort_values('score',ascending=False))
            list = tag_slporesum[tag_slporesum['sum'] >10].sort_values('score'ascending=False).head(10)
            st.subheader('태그별 평가가 좋은 대표 드라마 목록 입니다')
            select = st.selectbox('',list )
            st.dataframe(df_main[df['Tags'].str.contains(str(select),na=False)],)


        if status == '화제순':
            st.subheader('화제가 된 작품들의 태그입니다')
            st.dataframe(tag_slporesum[tag_slporesum['sum'] >10].loc[:,['review']].sort_values('review',ascending=False))
            list = tag_slporesum[tag_slporesum['sum'] >10].sort_values('review',ascending=Fals).head(10)
            st.subheader('태그별 드라마 목록 입니다')
            select = st.selectbox('',list )
            st.dataframe(df_main[df['Tags'].str.contains(str(select),na=False)],)


    if select_rank =='배우별' :
        actor_slporesum = pd.read_csv('data/actor_slporesum.csv',index_col='actors')

        if status == '인기순' :
            st.subheader('인기 작품에 많이 출연한 배우입니다')
            st.dataframe(actor_slporesum[actor_slporesum['sum'] >5].loc[:,['Popularity']].sort_values('Popularity'))
            list = actor_slporesum[actor_slporesum['sum'] >10].sort_values('Popularity').head(10)
            st.subheader('배우 필모그래피 보기')
            select = st.selectbox('',list )
            st.dataframe(df_main[df['actors'].str.contains(str(select),na=False)],)
        if status == '평점순':
            st.subheader('명작에 많이 출연한 배우 입니다')
            st.dataframe(actor_slporesum[actor_slporesum['sum'] >5].loc[:,['socre']].sort_values('socre',ascending=False))
            list = actor_slporesum[actor_slporesum['sum'] >5].sort_values('socre',ascending=False).head(10)
            st.subheader('배우 필모그래피 보기')
            select = st.selectbox('',list )
            st.dataframe(df_main[df['actors'].str.contains(str(select),na=False)],)            



        if status == '화제순':
            st.subheader('화제가 많이되는 작품에 출연한 배우입니다')
            st.dataframe(actor_slporesum[actor_slporesum['sum'] >5].loc[:,['review']].sort_values('review',ascending=False))
            list = actor_slporesum[actor_slporesum['sum'] >5].sort_values('review',ascending=False).head(10)
            st.subheader('배우 필모그래피 보기')
            select = st.selectbox('',list )
            st.dataframe(df_main[df['actors'].str.contains(str(select),na=False)],)



