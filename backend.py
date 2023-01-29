import requests

API_KEY = 'f87e88970ee6293f9065b93092cf37aa'


def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filter_data = data['list'][:8 * forecast_days]
    return filter_data


if __name__ == "__main__":
    print(len(get_data('tirana', 2)))
