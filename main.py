import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:")
days = st.slider(label="Forecast days", min_value=1, max_value=5, help="please select the number of days")
data_required = st.selectbox(label="Select type of data to view", options=('Temperature', 'Sky Conditions'))

if place:
    data = get_data(place, days)
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
        st.image(sky_images, width=150)
