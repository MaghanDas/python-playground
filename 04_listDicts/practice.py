

# A dictionary is a collection of key-value pairs, where each key is unique and maps to a value.
# Dictionaries are defined using curly braces {} and key-value pairs are separated by commas.
# Keys can be of any immutable type (like strings, numbers, tuples), while values can be of any type (including lists, other dictionaries, etc.).
# Dictionaries are mutable, meaning you can add, modify, or remove key-value pairs after the dictionary has been created.
# Dictionaries are unordered collections, meaning that the order of key-value pairs is not guaranteed (although from Python 3.7 onwards, they maintain insertion order).
# You can access values in a dictionary using their corresponding keys, and you can also loop through the dictionary to access keys and values.   

# practicing dictionaries and lists

number = [1, 2, 3, 4, 5]
squares = {x: x*x for x in number}
print(squares)
print(type(squares))

text = "apple banana apple orange banana apple"
word_count = {word: text.count(word) for word in text.split()}
print(word_count)

