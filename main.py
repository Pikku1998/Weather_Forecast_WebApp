import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:")
days = st.slider(label="Forecast days", min_value=1, max_value=5, help="please select the number of days")
data_required = st.selectbox(label="Select type of data to view", options=('Temperature', 'Sky Condition'))

st.subheader(f"{data_required} for the next {days} days in {place}")
