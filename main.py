import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:", placeholder='Please enter a city name')
days = st.slider(label="Forecast days", min_value=1, max_value=5, help="please select the number of days")
data_required = st.selectbox(label="Select type of data to view", options=('Temperature', 'Sky Conditions'))

if place:
    data = get_data(place, days)

    if data != 'city not found':
        st.subheader(f"{data_required} for the next {days} days in {place.title()}")

        if data_required == 'Temperature':
            x_axis_days = [item['dt_txt'] for item in data]
            y_axis_temp = [each['main']['temp'] for each in data]
            figure = px.line(x=x_axis_days, y=y_axis_temp, labels={'x': "Days", 'y': "Temperature (C)"})
            st.plotly_chart(figure)

        if data_required == 'Sky Conditions':
            sky_conditions = [item['weather'][0]['main'] for item in data]
            image_dict = {'Clear': 'images/clear.png',
                          'Clouds': 'images/cloud.png',
                          'Rain': 'images/rain.png',
                          'Snow': 'images/snow.png'}
            sky_images = [image_dict[item] for item in sky_conditions]
            image_captions = [item['dt_txt'] for item in data]
            st.image(sky_images, caption=image_captions, width=150)

    else:
        st.subheader("City not found, Please enter a valid city name.")
