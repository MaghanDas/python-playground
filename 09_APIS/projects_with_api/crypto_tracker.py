
# CRYPTO TRACKER: 
# concepts used: Multiples apis calls 
# looping through apis
# building a price dashboard

import requests
url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum,dogecoin",
    "vs_currencies": "usd"
}

response = requests.get(url, params = params)
data = response.json()
# print(data)
for crypto in data:
    print(crypto.upper() + ": $" + str(data[crypto]["usd"]))