import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:")
days = st.slider(label="Forecast days", min_value=1, max_value=5, help="please select the number of days")
data_required = st.selectbox(label="Select type of data to view", options=('Temperature', 'Sky Condition'))

st.subheader(f"{data_required} for the next {days} days in {place}")


figure = px.line(x=[1, 2, 3, 4, 5], y=[27, 29, 26, 24, 30], labels={'x': "Days", 'y': "Temperature (C)"})
st.plotly_chart(figure)
