import streamlit as st
import pandas as pd

#st.title("Website Developing using Python")
#st.header("🌶️Website Developing using Python🌶️")

dt=pd.read_csv('./data/Raisin.csv')

st.subheader("ข้อมูลRaisin")
st.write(dt.head(10))

st.subheader("ข้อมูลRaisin")
st.write('ผลรวม')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['Area'].sum())
cl2.write(dt['ConvexArea'].sum())
cl3.write(dt['Extent'].sum())
cl4.write(dt['Perimeter'].sum())

st.write('ค่าเฉลี่ย')
cl11,cl12,cl13,cl14=st.columns(4)
cl11.write(dt['Area'].mean())
cl12.write(dt['ConvexArea'].mean())
cl13.write(dt['Extent'].mean())
cl14.write(dt['Perimeter'].mean())

st.write('ค่ามากที่สุด')
cl21,cl22,cl23,cl24=st.columns(4)
cl21.write(dt['Area'].max())
cl22.write(dt['ConvexArea'].max())
cl23.write(dt['Extent'].max())
cl24.write(dt['Perimeter'].max())

import numpy as np
import matplotlib.pyplot as plt
labels = ['Area', 'ConvexArea','Extent','Perimeter']
sizes = [35,25,15,25]
explode = (0, 0.1,0,0) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
st.pyplot(fig1)

st.write('ค่าน้อยที่สุด')
cl31,cl32,cl33,cl34=st.columns(4)
cl31.write(dt['Area'].min())
cl32.write(dt['ConvexArea'].min())
cl33.write(dt['Extent'].min())
cl34.write(dt['Perimeter'].min())

st.write("Line_Chart")
cc=[3,8,1,10]
st.line_chart(cc)