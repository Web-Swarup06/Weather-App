import streamlit as st
import requests

#API KEY
api="a1b6bf1a284e457f7f59dd485b2b072e"

#GET DATA FROM OPEN WEATHER WEBSITE
def place_name(name):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api}&units=metric"
    r = requests.get(url)

    if r.status_code == 200:
        weather_data = r.json()
        return weather_data
    
#PAGE SETTINGS
st.set_page_config(page_title="Weather Forecast", page_icon="🌤️", layout="centered")

#TITLE
st.title("🌦️ Weather Forecasting App")

#CITY NAME INPUT
st.subheader('Type the city name')
name = st.text_input('',placeholder="e.g. Kolkata, London, Tokyo")

if st.button('Get Weather'):
    w_info = place_name(name)

    if w_info:
        st.metric(label="📍 City Name", value=f"{w_info['name']}")

        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

        with col1:
            st.metric(label="🌍 Longitude", value=f"{w_info['coord']['lon']}")
            
        with col2:
            st.metric(label="🧭 Latitude", value=f"{w_info['coord']['lat']}")

        with col3:
            st.metric(label="🌡️ Temperature", value=f"{w_info['main']['temp']}")

        with col4:
            st.metric(label="🌡️ Feels Like", value=f"{w_info['main']['feels_like']}")

        with col5:
            st.metric(label="☀️ Weather", value=f"{w_info['weather']['description']}")

        with col6:
            st.metric(label="💧 Humidity", value=f"{w_info['main']['humidity']}")

        with col7:
            st.metric(label="💨 Wind Speed", value=f"{w_info['wind']['speed']}")

            

            

