# some interview questions on dictionaries 

# question:1: frequency counter 
nums = [1,1, 2,3,3,3,4]

freq={}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)
# explanation of the code:
#  freq[n] = freq.get(n, 0) + 1 what does it do?
# This line of code is used to count the frequency of each element in the list `nums
# # Here's how it works:
# 1. `freq.get(n, 0)`: This part of the code checks if the
# key `n` exists in the dictionary `freq`. If it does, it returns the current count of that key. If it doesn't exist, it returns `0` (the default value provided).    
# 2. `freq.get(n, 0) + 1`: This adds `1` to the current count of the key `n`. If the key doesn't exist, it effectively starts counting from `1` (since `0 + 1` equals `1`).
# 3. `freq[n] = ...`: This assigns the new count back to the key `n` in the dictionary `freq`. If the key already exists, it updates the count; if it doesn't exist, it creates a new key-value pair with the count of `1`.

# hashmap look up: (O(1) time complexity)
# two sum problem 
nums = [2, 7, 11, 15]
target = 9 
lookup = {}

for i, num in enumerate(nums):
    diff = target - num
    if diff in lookup:
        print([lookup[diff], i])
    
    lookup[num] = i

# enumerate(nums) is used to get both the index and the value of each element in the list `nums`.
# `diff = target - num` calculates the difference between the target and the current number.
# `if diff in lookup:` checks if this difference has already been seen and stored in the `lookup` dictionary.
# If it exists, it means we have found the two numbers that add up to the target, and we print their indices.
# Finally, `lookup[num] = i` stores the current number and its index in the `lookup` dictionary for future reference.

# grouping data problem: GROUP ANAGRAM 
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}
for word in words: 
    key = ''.join(sorted(word))
    groups.setdefault(key, []).append(word)

print(groups.values())

# another simple code 
from collections import defaultdict
groups = defaultdict(list)
for word in words:
    key = ''.join(sorted(word))
    groups[key].append(word)

print(groups.values())

# explanation: 
# 1. `key = ''.join(sorted(word))`: This line sorts the characters of the word and joins them back into a string. This sorted string serves as a unique key for all anagrams. For example, "eat", "tea", and "ate" will all produce the same key "aet".
# 2. `groups.setdefault(key, []).append(word)`: This line uses the `setdefault` method to ensure that there is a list associated with the key in the `groups`
# dictionary. If the key does not exist, it initializes it with an empty list. Then, it appends the original word to the list corresponding to that key.
# # 3. `print(groups.values())`: This line prints the values of the `groups
# dictionary`, which are lists of anagrams grouped together. Each list contains words that are anagrams of each other.


# advanced dictionary patterns:
# pattern: inverted index : used in search engine 
documents = {
    1: "python is great",
    2: "I love python",
    3: "python programming"
}

index = {}

for doc_id, text in documents.items():
    for word in text.split():
        index.setdefault(word,[]).append(doc_id)

print(index)

#  Pattern 2: caching(Huge in real systems)
cache = {}
def slow_square(n):
    if n in cache:
        return cache[n]
    else:
        result = n * n
        cache[n] = result
        return result

# pattern:3 dispatch table 

operations = {
    "ADD": lambda x, y: x + y,
    "SUB": lambda x, y: x - y,
    "MUL": lambda x, y: x * y,
    "DIV": lambda x, y: x / y if y != 0 else ""
}
print(operations["ADD"](5, 3))  # Output: 8

