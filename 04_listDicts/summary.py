
# 📌 1. Lists (Ordered, Mutable, Allows Duplicates)
# A list is an ordered collection that is mutable (can be changed) and allows duplicate values.

# ✅ Key Points:
# ✔ Ordered (items have a fixed position)
# ✔ Mutable (can modify elements)
# ✔ Allows duplicate values

fruits = ["apple", "banana", "cherry", "apple"]  # Allows duplicates
fruits[1] = "orange"  # Lists are mutable
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'apple']

# 🔹 Common Operations
fruits.append("grape")  # Adds an item to the end
fruits.remove("apple")  # Removes the first occurrence of "apple"
print(len(fruits))  # Gets the number of elements


# 📌 2. Tuples (Ordered, Immutable, Allows Duplicates)
# A tuple is similar to a list but is immutable (cannot be changed after creation).

# ✅ Key Points:
# ✔ Ordered (items have a fixed position)
# ✔ Immutable (cannot modify elements)
# ✔ Allows duplicate values

coordinates = (10, 20, 30)  # Tuple with 3 elements
print(coordinates[1])  # Output: 20

# This will cause an error because tuples are immutable
# coordinates[1] = 50  ❌ ERROR
print(len(coordinates))  # Gets the number of elements
print(coordinates.count(10))  # Counts occurrences of a value


# 📌 3. Dictionaries (Key-Value Pairs, Mutable, No Duplicates in Keys)
# A dictionary stores data in key-value pairs and is unordered before Python 3.7, but ordered from Python 3.7+.

# ✅ Key Points:
# ✔ Uses key-value pairs
# ✔ Mutable (can modify values)
# ✔ Keys must be unique, but values can be duplicates

# 🔹 Example
book = {
    "title": "Harry Potter",
    "author": "J.K. Rowling",
    "year": 2002
}
print(book["title"])  # Output: Harry Potter

book["year"] = 2004  # Modifying an existing key
book["rating"] = 9.1  # Adding a new key-value pair
print(book.keys())  # Get all keys
print(book.values())  # Get all values
print(book.items())  # Get all key-value pairs

# 📌 4. Sets (Unordered, Unique Elements, Mutable)
# A set is an unordered collection of unique elements.

# ✅ Key Points:
# ✔ Unordered (no fixed position)
# ✔ Only unique values (no duplicates)
# ✔ Mutable (can add/remove elements)

numbers = {1, 2, 3, 3, 4, 5}  # Duplicates are automatically removed
print(numbers)  # Output: {1, 2, 3, 4, 5}

numbers.add(6)  # Add an element
numbers.remove(3)  # Remove an element
print(2 in numbers)  # Check if 2 is in the set
evens = {2, 4, 6, 8}
odds = {1, 3, 5, 7}
print(evens | odds)  # Union (all elements)
print(evens & odds)  # Intersection (common elements)
print(evens - odds)  # Difference (elements in evens but not in odds)

# 🔹 Quick Comparison Table
# Feature     	                 Lists   	        Tuples 	     Dictionaries	                  Sets
# Ordered?	                 ✅ Yes	    ✅ Yes  	  ✅ (Python 3.7+)	     ❌ No
# Mutable?	                ✅ Yes      	❌ No	 ✅ Yes                         ✅ Yes
# Allows Duplicates?  ✅ Yes	      ✅ Yes	   ❌No (keys)                ❌ No
# Key-Value Pairs?     ❌ No       ❌ No     ✅ Yes	                    ❌ No
# Indexing Allowed?	 ✅ Yes	     ✅ Yes    ❌No (Uses Keys)	  ❌ No



# 🔥 Final Challenge
# Create a list of 5 favorite movies.
# Convert it into a tuple.
# Create a dictionary with "title", "year", and "genre".
# Store multiple genres in a set and check if "Action" is included