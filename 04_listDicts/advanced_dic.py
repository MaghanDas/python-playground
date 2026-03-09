from collections import defaultdict
from collections import Counter

# Advanced Dictionary Operations

# 1. Dictionary Comprehension
squares = {x: x**2 for x in range(5)}
print("Squares:", squares)

# 2. Conditional Dictionary Comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Even squares:", even_squares)

# 3. Merging Dictionaries (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print("Merged:", merged)

# 4. Using setdefault() to handle missing keys
config = {'debug': True}
config.setdefault('timeout', 30)
print("Config:", config)

# 5. Using get() with default values
user = {'name': 'Alice'}
age = user.get('age', 'Not specified')
print("Age:", age)

# 6. fromkeys() - Create dictionary with default values
keys = ['x', 'y', 'z']
coords = dict.fromkeys(keys, 0)
print("Coords:", coords)

# 7. Nested dictionary operations
person = {
    'name': 'Bob',
    'address': {'city': 'NYC', 'zip': '10001'},
    'hobbies': ['reading', 'coding']
}
print("City:", person['address']['city'])

# 8. Dictionary iteration techniques
print("\nIteration techniques:")
for key, value in person.items():
    print(f"  {key}: {value}")

# 9. Updating multiple keys at once
person.update({'age': 30, 'email': 'bob@example.com'})
print("Updated person:", person)

# 10. Using collections.defaultdict
word_count = defaultdict(int)
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
for word in words:
    word_count[word] += 1
print("Word count:", dict(word_count))

# 11. Using collections.Counter
counter = Counter(words)
print("Counter:", counter)
print("Most common:", counter.most_common(2))