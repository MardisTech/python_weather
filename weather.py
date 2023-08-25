import requests
import config

# API_KEY = "config.API_KEY"     in local project folder
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&APPID={config.API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    tempFahrenheit = round((((float(data['main']['temp']) - 273.15) *9) / 5) + 32, 2)
    print(f"In {city} the temperature is {tempFahrenheit} Fahrenheit, with {data['weather'][0]['description']}")
else:
    print("an error occured")


