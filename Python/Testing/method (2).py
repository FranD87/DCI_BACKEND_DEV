import requests

def get_weather(city: str) -> str:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=43b266f8cb711ed5efe421236addda4f&units=metric'
    response = requests.get(url)
    if response.status_code != 200:
        msg = f'Request failed with code {response.status_code}'
        raise RuntimeError(msg)
    temperature = response.json()['main']['temp']
    if temperature > 15:
        return 'Good'
    else:
        return 'Bad'

