import requests

# API = Application Programming Interface: 
# it allows programms to talk to other programs over the internet 

# Your Python script → API request → Server → Response (data)

# Example real APIs:
# Weather API
# Cryptocurrency prices
# GitHub data
# Maps
# AI APIs
# Most APIs return JSON, which is basically a Python dictionary.

# example response:  in Json
# {     
#     "name": "Das",
#     "age": 23,
#     "city": "Budapest"
# }

# in python it becomes : dictionary
# person = {
#     "name": "Das",
#     "age": 23,
#     "city": "Budapest"
# }

# working in python: install requests libray 
# pip install requests
# import as above in this file  and then we can make API calls

url = "https://api.github.com"
response = requests.get(url)
print(response.status_code) # 200 means success 
# print(response.text) # raw text response
# data = response.json() # parse JSON response into a Python dictionary
# print(data) # print the parsed data
# print(type(data))
# print(data["current_user_url"])


# Calling a Real Rest Api : 
# url = "https://api.coindesk.com/v1/bpi/currentprice.json"
# response = requests.get(url)
# data = response.json()
# print(data)
# print(response.status_code)

# using Query Parameters: 
url = "https://api.agify.io"

params = {
    "name": "alex"
}

response = requests.get(url, params=params)
data = response.json()
print(data)
print(data["age"])

