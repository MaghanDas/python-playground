
# Weather CLI APP 
# concepts used, API requests, Json parsing, dictionary navigation and cli input 

import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 47.4979,
    "longitude": 19.0402,
    "current_weather": True
}

response = requests.get(url, params=params)
# print(response)
if response.status_code == 200:
    data = response.json()
    # print(data)
    current_weather = data["current_weather"]
    print("Current temperature in Budapest: ", current_weather["temperature"], "°C")

else:
    print("Error fetching weather data", response.status_code)
    
    