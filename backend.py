import requests
import os

API_KEY = os.getenv("WEATHER_API_KEY")


def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data['message'] == 'city not found':
        return 'city not found'
    else:
        filtered_data = data['list'][:8 * forecast_days]
        return filtered_data
