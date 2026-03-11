
# problem : 1 find expensive cryptocurrencies 
import requests

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

# print(response.json())
for curr in data:
    if curr["current_price"] > 1000:
        print(curr["name"], ":", curr["current_price"])

username= input("enter github username: ")
url = "https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

