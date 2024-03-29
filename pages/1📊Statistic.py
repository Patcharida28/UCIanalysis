import streamlit as st
import pandas as pd

#st.title("Website Developing using Python")
#st.header("🌶️Website Developing using Python🌶️")

dt=pd.read_csv('./data/Raisin.csv')

lottie_url_hello = "https://lottie.host/fdd490d8-353e-4c58-a976-abf5f9c99261/mcARPoQsZF.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")

st.subheader("🍖🍖สถิติข้อมูลแสดงภาพพันธุ์ของลูกเกด🍖🍖")
st.write(dt.head(50))