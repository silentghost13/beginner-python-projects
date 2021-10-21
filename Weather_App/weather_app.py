import requests
from pprint import pprint
#https://www.youtube.com/watch?v=SqvVm3QiQVk&t=40s
API_key = 'b979cba50050174b8c3044fcaaf5eced'

city_name = input('Enter a city : ')

base_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + API_key

weather_data = requests.get(base_url).json()

pprint(weather_data)