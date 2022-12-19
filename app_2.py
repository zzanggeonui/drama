import streamlit as st
import pandas as pd
import numpy as np

def run_2_app() :
    df= pd.read_csv('data/realeditdrama.csv',index_col =0)
    df_genre= pd.read_csv('data/gentttttt.csv',index_col = 'genre')
    df_main = df.loc[:,['drama_name','Episodes','platforms']]
    df_actor = pd.read_csv('data/actor_list.csv',index_col = 'actor')
    df_tag = pd.read_csv('data/tag_list.csv')

    select = st.selectbox('장르선택',df_genre)

    filter = df_main[df['Genres'].str.contains(str(select),na=False)]
    
    select2 =  st.selectbox('배우선택',df_actor)
    select3 =  st.multiselect('tag선택',df_tag)
    st.dataframe(filter[df['actors'].str.contains(str(select2),na=False)],)
    

    st.dataframe(df_main[df['actors'].str.contains(str(select2),na=False)],)
