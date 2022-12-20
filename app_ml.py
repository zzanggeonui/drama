import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

def run_ml_app() :
    po_sc = pd.read_csv('data/popula_score.csv')    
    genre_list = pd.read_csv('data/genre_sum.csv').head(10)
    fig = px.pie(genre_list, 'genre','sum',title='장르별 차트')
    st.plotly_chart(fig)
    
    



