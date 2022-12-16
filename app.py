import streamlit as st
import pandas as pd

def main() :
    df= pd.read_csv('data/editdrama.csv',index_col =0)
    df_genre= pd.read_csv('data/gentttttt.csv',index_col = 'genre')

    df_main = df.loc[:,['drama_name','actors','imdb_description','Genres']]
    selected_list = st.multiselect('장르를 선택하세요',df_genre )
    
    if len(selected_list) != 0 :

        st.dataframe(df[df['Genres'].str.contains(str('war'),na=False)])
        st.dataframe(df_main[df['Genres'].str.contains(str('war'),na=False)])
        st.(selected_list)

if __name__ == '__main__':
    main()