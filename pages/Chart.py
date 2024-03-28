import streamlit as st
import pandas as pd

st.title("Website Developing using Python")
st.header("🌶️Website Developing using Python🌶️")

st.subheader("🍔Patcharida Choomchoo🍔")
st.image('patch.jpg')

dt=pd.read_csv('./data/iris.csv')

dt=pd.read_csv('./data/iris.csv')

st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))
#Index(['sepal.length', 'sepal.width', 'petal.length', 'petal.width',
#       'variety'],

st.write("Area_Chart")
a=dt['Area'].mean()
b=dt['ConvexArea'].mean()
c=dt['Extent'].mean()
d=dt['Perimeter'].mean()
dxt=[a,b,c,d]
cxx=pd.DataFrame(dxt,index=["Area", "ConvexArea", "Extent","Perimeter"])
st.area_chart(cxx)

st.write('ค่ามากที่สุด')
cl21,cl22,cl23,cl24=st.columns(4)
cl21.write(dt['Area'].max())
cl22.write(dt['ConvexArea'].max())
cl23.write(dt['Extent'].max())
cl24.write(dt['Perimeter'].max())

import numpy as np
import matplotlib.pyplot as plt
labels = ['Men', 'Women','','']
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