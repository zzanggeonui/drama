import streamlit as st
import pandas as pd

def main() :
    df= pd.read_csv('data/editdrama.csv',index_col =0)
    df_genre= pd.read_csv('data/genre_list.csv',index_col = 'genre')

    df_main = df.loc[:,['drama_name','Episodes','platforms','actors','imdb_description','Genres']]

    selected_list = st.multiselect('장르를 선택하세요',df_genre )
    st.dataframe(df[df['Genres'].str.contains(str(selected_list),na=False)])
    st.dataframe(df_main[df['Genres'].str.contains(str(selected_list),na=False)])


if __name__ == '__main__':
    main()