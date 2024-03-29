import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
st.title("การประยุกต์ใช้งาน Machine learning บนเว็บ")
st.subheader(" By นางสาวพัชริดา ชุ่มชู สาขาวิชาวิทยาการคอมพิวเตอร์ คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏนครปฐม")

lottie_url_hello = "https://lottie.host/a4a8e206-d582-4211-9292-e6dbdaf428b1/NbkG79OEyW.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")

st.page_link("home.py", label="หน้าแรก", icon="🏠")

st.page_link("pages/1📊Statistic.py", label="การนำเสนอข้อมูลชนิดของภาพพันธ์ลูกเกดด้วยการจินตทัศน์ข้อมูล", icon="1️⃣")
st.page_link("pages/2📈Chart.py", label="การนำเสนอข้อมูลชนิดของภาพพันธ์ลูกเกดด้วยสถิติ", icon="2️⃣", disabled=False)
st.page_link("pages/3🧭KNNClassification.py", label="การนำเสนอข้อมูลชนิดของภาพพันธ์ลูกเกดด้วย KNN-lassifier", icon="3️⃣", disabled=False)
st.page_link("pages/4🏝️DecisionTree.py", label="การนำเสนอข้อมูลชนิดของภาพพันธ์ลูกเกดด้วย DecisionTree", icon="4️⃣", disabled=False)
st.page_link("pages/5🍌NaiveBaye.py", label="การนำเสนอข้อมูลชนิดของภาพพันธ์ลูกเกดด้วย NaiveBaye", icon="5️⃣", disabled=False)
st.page_link("pages/6🦊Regression.py", label="การนำเสนอข้อมูลชนิดของภาพพันธ์ลูกเกดด้วย Regression", icon="6️⃣", disabled=False)
st.page_link("https://archive.ics.uci.edu/dataset/850/raisin", label="อ้างอิงข้อมูลภาพพันธ์ลูกเกด(ชุดข้อมูล)", icon="🌎")