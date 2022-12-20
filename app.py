import streamlit as st
import pandas as pd
from app_home import run_home_app
from app_2 import run_2_app


def main() :
    st.title('드라마')
    menu = ['홈','상세검색','차트']
    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == '홈' :
        pass
        

    elif choice == '상세검색' :
        run_home_app()

    elif choice == '차트':
        run_2_app()


if __name__ == '__main__':
    main()