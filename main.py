import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the next days")

place=st. text_input("Place")
days=st.slider("Forecast days", 1, 5, 1)
option=st.selectbox("Select data to view:", ("Temperature", "Sky"))

if place !="" and option!="":
    if days==1:
        st.subheader(f"{option} for the next day in {place}")
    else:
        st.subheader(f"{option} for the next {days} days in {place}")


if option=="Temperature":
    dates, temp= get_data(place, days)

    figure=px.line(x=dates, y=temp, labels={"x": "Dates", "y": "Temperature"})
    st.plotly_chart(figure)