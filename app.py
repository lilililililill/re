import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv('기숙사수용현황분석.csv')
#st.dataframe(data)

#st.write('기숙사현황')

df. data[data['학교종류']=='대학교']
num1= len(df['학교'].unique())
num2= len(df[df['설립구분'] !=  '사립']['학교'].unique())
num3 = len(df[df['설립구분'] == '사립']['학교'].unique())

col1, col2, col3 = st.columns(3)
col1.metric("전국대학수", num1, "")
col2.metric("국공립학교", num2, num2/num1 * 100)
col3.metric("사립", num3, num3/num1 * 100)

st.sidebar:
    gunum = st.radio("학교 구분",("사립", "국공립"))
    if gunum == '사립'
        st.write(gubun)
    else:
        st.write(gubun)


