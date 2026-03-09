
# MINI PROJECT: Country information App
import json
import requests 

country = "hungary"
url = f"https://restcountries.com/v3.1/name/{country}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    info = data[0]
else:
    print("Error fetching country information", response.status_code)

print(info)
print("Country: ", info["name"]["common"])
print("Capital: ", info["capital"][0])
print("Population: ", info["population"])

# common status codes:
# 200 → success
# 404 → not found
# 401 → unauthorized
# 500 → server error

url = "https://httpbin.org/post"
data = {
    "username": "alex",
    "password": "123456"
}

response = requests.post(url, json=data)

print(response.json())
print(json.dumps(response.json(), indent=4)) # this helps see the structure