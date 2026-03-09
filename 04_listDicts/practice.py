

# A dictionary is a collection of key-value pairs, where each key is unique and maps to a value.
# Dictionaries are defined using curly braces {} and key-value pairs are separated by commas.
# Keys can be of any immutable type (like strings, numbers, tuples), while values can be of any type (including lists, other dictionaries, etc.).
# Dictionaries are mutable, meaning you can add, modify, or remove key-value pairs after the dictionary has been created.
# Dictionaries are unordered collections, meaning that the order of key-value pairs is not guaranteed (although from Python 3.7 onwards, they maintain insertion order).
# You can access values in a dictionary using their corresponding keys, and you can also loop through the dictionary to access keys and values.   

# practicing dictionaries and lists

from unicodedata import name


number = [1, 2, 3, 4, 5]
squares = {x: x*x for x in number}
print(squares)
print(type(squares))

text = "apple banana apple orange banana apple"
word_count = {word: text.count(word) for word in text.split()}
print(word_count)


# dictionary (hashmaps) is data structure that allows
# very fast lookups, insertions, and deletions based on keys. 
# ex: person = {
#     "name": "Das",
#     "age": 23,
#     "city": "Budapest"
# }
# intenernally python: 
# index | key    | value
# -----------------------
# 3     | name   | Das
# 7     | age    | 23
# 1     | city   | Budapest

# that index comes from hash function that takes the key and returns a unique index for it.
# hash function is a function that takes an input (or "key") and returns a fixed-size string of bytes.
# hash (name) # output then python converts into an index isnide th hash table 

# when we write person["name"] = "das"
# python calculate of "name" and converts to index: 
# and then store key-value pair at that index in the hash table.

# hash collisition when two keys produces the same index.
# keys must be immutable so their hash never chnages
# list as key can't be allowed because they are mutable and their hash can change, which would cause issues in the hash table.
