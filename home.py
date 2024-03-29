import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/78241b7d-fc55-4aae-9b67-7b6110f85dd3/7Bt8aUYObq.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")

st.page_link("home.py", label="หน้าแรก", icon="🏠")

st.page_link("pages/1📊Statistic.py", label="การนำเสนอข้อมูลชนิดของภาพพันธ์ลูกเกดด้วยการจินตทัศน์ข้อมูล", icon="1️⃣")
st.page_link("pages/2📈Chart.py", label="การนำเสนอข้อมูลชนิดของภาพพันธ์ลูกเกดด้วยสถิติ", icon="2️⃣", disabled=False)
st.page_link("pages/3🧭Classification.py", label="การนำเสนอข้อมูลชนิดของภาพพันธ์ลูกเกดด้วยKNNClassifier", icon="2️⃣", disabled=False)
st.page_link("pages/4🏝️DecisionTree.py", label="การนำเสนอข้อมูลชนิดของภาพพันธ์ลูกเกดด้วยDecisionTree", icon="2️⃣", disabled=False)
st.page_link("https://archive.ics.uci.edu/dataset/850/raisin", label="อ้างอิงข้อมูลภาพพันธ์ลูกเกด(ชุดข้อมูล)", icon="🌎")