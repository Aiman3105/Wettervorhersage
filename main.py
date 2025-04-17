import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the next days")

place=st. text_input("Place")
days=st.slider("Forecast days", 1, 5, 1)
option=st.selectbox("Select data to view:", ("Temperature", "Sky"))


if option=="Temperature" and place!="":
    try:
        dates, temp, sky = get_data(place, days)
        figure = px.line(x=dates, y=temp,
                         labels={"x": "Dates", "y": "Temperature"})
        if place != "" and option != "":
            if days == 1:
                st.subheader(f"{option} for the next day in {place}")
            else:
                st.subheader(f"{option} for the next {days} days in {place}")

        st.plotly_chart(figure)
    except KeyError:
        st.write("There is no data for the entered location")

if option=="Sky":
    try:
        if place != "" and option != "":
            if days == 1:
                st.subheader(f"{option} for the next day in {place}")
            else:
                st.subheader(f"{option} for the next {days} days in {place}")
        dates, temp, sky = get_data(place, days)
        cols = st.columns(6)
        image_map = {
            "Clear": "images/clear.png",
            "Rain": "images/rain.png",
            "Clouds": "images/cloud.png",
            "Snow": "images/snow.png"}



        for index, item in enumerate(sky):
            col = cols[index % 6]
            with col:
                if item in image_map:
                    st.image(image_map[item], caption=dates[index])
    except KeyError:
        st.write("There is no data for the entered location")


