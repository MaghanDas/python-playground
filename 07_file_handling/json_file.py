
# working with json files

import json 

# ✅ Writing to a JSON File
user = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "active": True
}

with open("user.json", "w") as file:
    json.dump(user, file, indent = 4)  # indent for pretty printing

# ✅ Reading from a JSON File
with open("user.json", "r") as file:
    data = json.load(file) # dictionary backs.

# print(data)
# print("Name:", data["name"])
# print("Age:", data["age"])
# print("Skills:", data["skills"])
# print("Active:", data["active"])


# JSON <-> String(wihout files)
json_string = json.dump(user) # converts dict to json string
print(json_string)
python_dict = json.loads(json_string) # converts json string back to dict
print(python_dict)

# production tip: handle missig files gracefully 
import os 


def load_config(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    with open(path, "r") as file:
        return json.load(file)
