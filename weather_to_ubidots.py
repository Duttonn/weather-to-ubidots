import os
import requests

CITY = "Saint-Cyr,FR"
OWM_API_KEY = os.environ["OWM_API_KEY"]
UBIDOTS_TOKEN = os.environ["UBIDOTS_TOKEN"]
DEVICE_LABEL = "weather-api"

owm_url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OWM_API_KEY}&units=metric"
response = requests.get(owm_url)
print("OpenWeatherMap status:", response.status_code)
print("OpenWeatherMap response:", response.text)

# Check for a valid response
if response.status_code != 200:
    raise Exception("Failed to get weather data from OpenWeatherMap")

data = response.json()

temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]

ubidots_url = f"https://stem.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}"
payload = {
    "temperature": temperature,
    "humidity": humidity,
    "pressure": pressure
}
headers = {
    "X-Auth-Token": UBIDOTS_TOKEN,
    "Content-Type": "application/json"
}
res = requests.post(ubidots_url, headers=headers, json=payload)
print("Ubidots status:", res.status_code)
print("Ubidots response:", res.text)
