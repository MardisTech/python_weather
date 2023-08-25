import requests

API_KEY = "1200342a464f1ee5062eba952d4f255a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&APPID={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(f"In {city}, the temperature is {data['main']['temp']} kelvin, with {data['weather'][0]['description']}")
else:
    print("an error occured")


