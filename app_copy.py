import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt


def run_sc_app() :
    df = pd.read_csv('data/realeditdrama.csv', thousands = ',',index_col='Unnamed: 0')
    df_main = df.loc[:,['drama_name','Content Rating','scored by','score','Popularity','Episodes','Genres','Tags','platforms']]
    df_main.columns = ['제목','연령제한','화제순','평점순','인기순','에피소드수','장르','태그','플랫폼']

    st.title('항목별 상세 검색 페이지 입니다')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    platforms = df['platforms']
    platforms_list = []
    for x in platforms :
        x = x.split(',')
        for x2 in x :
            x2 = x2.strip(" ")
            x2 = x2.strip("''")
            platforms_list.append(x2)
    plat = pd.DataFrame(pd.DataFrame(data =platforms_list).value_counts()).rename(columns={0:'sum'}).reset_index().rename(columns={0:'platforms'}).drop(1,axis=0)
    plat.loc[len(plat)] = ['전체',1000]
    plat = plat.sort_values('sum',ascending=False)

    
    status = st.radio('',['인기순','평점순','화제순'])
    st.subheader('플랫폼 선택')
    plat_select = st.selectbox('',plat)

    st.subheader('평점선택')
    score = st.select_slider('', options=[4,5,6,7,8,9,10,'전체'],value='전체')

      




    if status != '인기순' :
        if plat_select != '전체':
            selectframe = pd.DataFrame(df_main[df_main['플랫폼'].str.contains(str(plat_select),na=False)].sort_values(status,ascending = False) )    
            if score != '전체':
                st.dataframe(selectframe[(df_main['평점순'] <= score ) & (df_main['평점순'] >= score -0.5 )])
            else:
                st.dataframe(selectframe.sort_values(status,ascending=False ))
        else :
            if score != '전체':
                st.dataframe(df_main[(df_main['평점순'] <= score ) & (df_main['평점순'] >= score -0.5 )])
            else:
                st.dataframe(df_main.sort_values(status,ascending=False ))
    else:
        if plat_select != '전체':
            selectframe = pd.DataFrame(df_main[df_main['플랫폼'].str.contains(str(plat_select),na=False)].sort_values(status) )
            if score != '전체':
                st.dataframe(selectframe[(df_main['평점순'] <= score ) & (df_main['평점순'] >= score -0.5 )])
            else:
                st.dataframe(selectframe.sort_values(status))
        else:
            
            if score != '전체' :
                st.dataframe(df_main.sort_values(status)[(df_main['평점순'] <= score ) & (df_main['평점순'] >= score -0.5 )])
            else:
                st.dataframe(df_main.sort_values(status ))


