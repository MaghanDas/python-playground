
# Dictionaries in Python:
# Dictionaries are unordered collections of key-value pairs. 
# They allow you to store and retrieve data efficiently using keys.

# creating dictionary:

person = {
  "Name": "Das",
   "Age": 23,
  "City": "Budapest"
}

# print(person) 
# print(person["Name"]) # das -> accessing values of dict person.
# print(person["Das"]) # key error

person["City"] = "Tokyo" # updating the value...
person["Profession"] = "student" # add a new key-value pair

# print(person)
# print(type(person)) # dict

# looping through dictionary 
# for key in person:
#     print("Key :", person[key])

# for key,value in person.items():
#   print(key, ":", value)


# Create a dictionary to represent a book with the following keys: title, author, year, genre.
# Add a new key-value pair: rating.
# Print out the title and rating of the book.
# Update the year of the book.
# Loop through the dictionary and print each key and its corresponding value.

book = { 
    "title": "Harry Potter",
    "author": "JK Rowling",
    "year": 2002,
    "genre": "Fantasy"
}

print(book)
book["rating"] = 9.10
print(book["title"])
print(book["rating"])
book["year"] = 2004

for key,value in book.items():
    print(key, ":",value)

# A new field "pages" (e.g., 500).
# A condition that prints "This is a long book!" if pages > 400.
# A nested dictionary where "publisher" has two subfields: "name" and "country"

book["pages"] = 500

if book["pages"] > 400:
    print("This is a long book!")
    

# Adding nested dictionary for publisher
book["publisher"] = { 
    "name": "New York Times",
    "country": "USA"
}

# Print the updated dictionary
for key, value in book.items():
    print(key, ":", value)

# Access nested dictionary values
print("Publisher Name:", book["publisher"]["name"])
print("Publisher Country:", book["publisher"]["country"])

# Add a list of "characters" inside the book dictionary (e.g., ["Harry", "Hermione", "Ron"]).
# Loop through the "characters" list and print each name.

# characters=["Harry", "Hermione", "Ron"]

book["characters"] = ["Harry", "Hermione", "Ron"]

for c in book["characters"]:
    print(c)

# Add another field called "available_formats", which is a set containing "Hardcover", "Paperback", and "Ebook".
# Print all available formats.
# Check if "Audiobook" is in the set. If not, print "Audiobook format is not available."

book["available_formats"] = {"Hardcover", "Paperback", "Ebook"}  # Adding a set

# Print available formats
print("Available Formats:", book["available_formats"])

# Check if 'Audiobook' is available
if "Audiobook" not in book["available_formats"]:
    print("Audiobook format is not available.")



# 🔹 Quick Comparison Table
# Feature     	                 Lists   	        Tuples 	     Dictionaries	                  Sets
# Ordered?	                 ✅ Yes	    ✅ Yes  	  ✅ (Python 3.7+)	    ❌ No
# Mutable?	                ✅ Yes      	❌ No	 ✅ Yes                  ✅ Yes
# Allows Duplicates?  ✅ Yes	      ✅ Yes	   ❌No (keys)                   ❌ No
# Key-Value Pairs?     ❌ No       ❌ No     ✅ Yes	                    ❌ No
# Indexing Allowed?	 ✅ Yes	     ✅ Yes    ❌No (Uses Keys)	            ❌ No

# practice: tasks 
print("******************")

car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2018
}

# built-in methods
# print(car.keys())
# print(car.values())
# print(car.items())
# car["color"] = "red"
# print(car.get("color"))

player = {
    "name": "john",
    "level": "Medium",
    "stats": {
        "hp": 200,
        "attack": 100,
        "defense": 320
    }
}

# some mini tasks solutions:

# print(player["stats"])
# print(player["stats"]["defense"])
# player["stats"]["attack"] += 5
# player["stats"]["speed"] = 10
# print(player["stats"])

# for key, value in player["stats"].items():
#     print(key,value)

pythoners = [
    {"Name": "Sree", "Age": 22},
    {"Name": "John", "Age": 21},
    {"Name": "Alex", "Age": 23}
]

# print all names only
# for i in range(0,len(pythoners)):
    # print(pythoners[i].get("Name"))
    # print(pythoners[i]["Name"])


# print users older than 22
# for i in range(0,len(pythoners)):
#     if(pythoners[i].get("Age")>22):
#         print(pythoners[i].get("Name"))

# add a new user david, 22
user = {
    "Name": "David",
    "Age": 22
}
pythoners.append(user)
print(pythoners)

