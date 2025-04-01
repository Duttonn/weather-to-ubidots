import os
import requests

# Read from environment variables (GitHub Secrets)
CITY = "Saint-Cyr,FR"
OWM_API_KEY = os.environ["OWM_API_KEY"]
UBIDOTS_TOKEN = os.environ["UBIDOTS_TOKEN"]
DEVICE_LABEL = "weather-api"

# Fetch weather data
owm_url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OWM_API_KEY}&units=metric"
response = requests.get(owm_url)
data = response.json()

temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]

# Send to Ubidots
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

print("Ubidots response:", res.status_code, res.text)
