import requests
api_key = "5bd5d2a0c4499b59d1f87906b30efdf0"
endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat":  6.723720,
    "lon": 3.163710,
    "appid": api_key,
}

response = requests.get(endpoint, params=parameters)
print(response.json())
