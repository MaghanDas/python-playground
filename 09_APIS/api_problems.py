
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

url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

print(repos)
max_starts = -1 
for repo in repos:
    if (repo["stargazers_count"] > max_starts):
        max_starts = repo["stargazers_count"]
        top_repo = repo["name"]

print(f"Top repository: {top_repo} with {max_starts} stars")