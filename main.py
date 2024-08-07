import streamlit as st

st.title("Welcome To Govind Enterprise Data Input")
name = st.text_input("Enter Your Name : ")
number = st.text_input("Enter Your Mobile Number : ")
address = st.text_area("Enter Your Address : ")
date = st.text_input("ENTER DATE : ")
numberofflats = st.selectbox("Enter The Number Of Flats :",(1,2,3,4)) 

button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Number : {number}
    Address : {address}
    Flats : {numberofflats}""")
