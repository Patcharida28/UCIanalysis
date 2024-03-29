import streamlit as st
import pandas as pd

#st.title("Website Developing using Python")
#st.header("🌶️Website Developing using Python🌶️")

dt=pd.read_csv('./data/Raisin.csv')

st.subheader("🍖🍖สถิติข้อมูลแสดงภาพพันธุ์ของลูกเกด🍖🍖")
st.write(dt.head(50))