import streamlit as st

st.title("Weather forecast for the next days")

place=st. text_input("Place")
days=st.slider("Forecast days", 1, 5, 1)
option=st.selectbox("Select data to view:", ("Temperature", "Sky"))

if place !="" and option!="":
    if days==1:
        st.subheader(f"{option} for the next day in {place}")
    else:
        st.subheader(f"{option} for the next {days} days in {place}")