import streamlit as st
import pandas as pd
from app_home import run_home_app
from app_eda import run_eda_app
from app_ml import run_ml_app

def main() :
    st.title('드라마')
    menu = ['홈','검색','상세검색','분석']
    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == '홈' :
        st.subheader('추천')
        

    elif choice == '검색' :
        run_home_app()

    elif choice == '상세검색':
        run_ml_app()

    elif choice == '분석':
        run_eda_app()


if __name__ == '__main__':
    main()