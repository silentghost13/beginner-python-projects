#https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
import requests 
import json

api_key = '271bc5eb995eab041bc0919bae99bc6c'
base_url = 'https://api.openweathermap.org/data/2.5/weather?q='
city_name = input('Enter city name : ')

complete_url = base_url + city_name + '&units=metric&appid=' + api_key 

response = requests.get(complete_url)

data = response.json()

if data['cod'] != '404':
	main = data['main']
	current_temperature = main['temp']
	current_pressure = main['pressure']
	current_humidity = main['humidity']
	z = data['weather']
	weather_description = z[0]['description']

	print(' Temperature (in celcius unit) = ' +
					str(current_temperature) +
		'\n atmospheric pressure (in hPa unit) = ' +
					str(current_pressure) +
		'\n humidity (in percentage) = ' +
					str(current_humidity) +
		'\n description = ' +
					str(weather_description))

else:
	print(' City Not Found ')
