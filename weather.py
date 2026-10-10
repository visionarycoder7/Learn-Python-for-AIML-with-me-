import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.2090&current=temperature_2m,weather_code"
response = requests.get(url)
data = response.json()

current = data["current"]
print("Temperature:", current["temperature_2m"], "°C")
print("Weather code:", current["weather_code"])