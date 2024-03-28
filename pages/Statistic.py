import streamlit as st
import pandas as pd

#st.title("Website Developing using Python")
#st.header("🌶️Website Developing using Python🌶️")

dt=pd.read_csv('./data/Raisin.csv')

st.subheader("🍖🍖สถิติข้อมูลแสดงภาพพันธุ์ของลูกเกด🍖🍖")
st.write(dt.head(100))

#st.subheader("สถิติข้อมูลRaisin")
#st.write('ผลรวม')
#cl1,cl2,cl3,cl4=st.columns(4)
#cl1.write(dt['Area'].sum())
#cl2.write(dt['ConvexArea'].sum())
#cl3.write(dt['Extent'].sum())
#cl4.write(dt['Perimeter'].sum())
#
#st.write("กราฟแท่ง")
#a=dt['Area'].sum()
#b=dt['ConvexArea'].sum()
#c=dt['Extent'].sum()
#d=dt['Perimeter'].sum()
#dx=[a,b,c,d]
#cx=pd.DataFrame(dx,index=["Area", "ConvexArea", "Extent","Perimeter"])
#st.bar_chart(cx)
#
#st.write('ค่าเฉลี่ย')
#cl11,cl12,cl13,cl14=st.columns(4)
#cl11.write(dt['Area'].mean())
#cl12.write(dt['ConvexArea'].mean())
#cl13.write(dt['Extent'].mean())
#cl14.write(dt['Perimeter'].mean())

#st.write("Area_Chart")
#a=dt['Area'].mean()
#b=dt['ConvexArea'].mean()
#c=dt['Extent'].mean()
#d=dt['Perimeter'].mean()
#dxt=[a,b,c,d]
#cxx=pd.DataFrame(dxt,index=["Area", "ConvexArea", "Extent","Perimeter"])
#st.area_chart(cxx)