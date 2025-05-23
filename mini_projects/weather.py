import requests

API_KEY = "93efd86f7acab286c57ea5f055d3a3e7"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"\n📍 Weather in {city.capitalize()}:")
    print(f"🌡️ Temperature: {temperature}°C")
    print(f"🤗 Feels like: {feels_like}°C")
    print(f"🌥️ Condition: {description.capitalize()}")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬️ Wind Speed: {wind_speed} m/s")
else:
    print("⚠️ City not found or API error. Please check the name and try again.")
