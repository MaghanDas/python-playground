

# Sets in python :  sets are unordered collections of unique elements .
#  they are useful when you need to store distinct values and peform set operations: (union, intersection,diff etc)

# creating a Set
fruits = {"apple", "banana", "cherry"}
# print(fruits)
# 🔸 No duplicates allowed! If you try to add "apple" again, it won’t be stored.

fruits.add("orange") # adds an element
fruits.remove("banana") # removes an element

# print(fruits)

#  Sets operations

# Union : Combining two Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}
# print(set1 | set2)  # {1, 2, 3, 4, 5, 6}

# Intersection : Common element in both Sets
# print(set1 & set2)  # {3}

# Difference: Elements in Set1 but not in Set2
# print(set1 - set2) # {1, 2}

# challenge
# Create two sets:
# evens = {2, 4, 6, 8, 10}
# odds = {1, 3, 5, 7, 9}
# Find the union and intersection of these sets.
# Remove a number from the evens set.
# Check if 7 is in the odds set.

evens = {2, 4, 6, 8, 10}
odds = {1, 3, 5, 7, 9}

# Union (All unique elements)
print("Union:", evens | odds)

# Intersection (Common elements)
print("Intersection:", evens & odds)  # This will be an empty set {}

# Remove an element from evens
evens.remove(10)
print("Updated evens:", evens)

# Check if 7 is in the odds set
if 7 in odds:
    print("7 is in the odds set!")
else:
    print("7 is not in the odds set.")


# 🔥 Challenge Extension
# Try adding another set called python
# primes = {2, 3, 5, 7, 11}
# Find the common numbers between primes and evens (intersection).
# Find the numbers in primes but not in odds (difference).
# Check if 11 is in primes, and print "11 is a prime number!" if true.

primes = {2, 3, 5, 7, 11}
print("common numbers between primes and evens ", primes & evens) 
print("numbers in primes but not in odds: ", primes -  odds) 

if 11 in primes:
    print("11 is a prime.")
else:
    print("not a prime")



# 🔹 Quick Comparison Table
# Feature     	                 Lists   	        Tuples 	     Dictionaries	                  Sets
# Ordered?	                 ✅ Yes	    ✅ Yes  	  ✅ (Python 3.7+)	     ❌ No
# Mutable?	                ✅ Yes      	❌ No	 ✅ Yes                         ✅ Yes
# Allows Duplicates?  ✅ Yes	      ✅ Yes	   ❌No (keys)                ❌ No
# Key-Value Pairs?     ❌ No       ❌ No     ✅ Yes	                    ❌ No
# Indexing Allowed?	 ✅ Yes	     ✅ Yes    ❌No (Uses Keys)	  ❌ No

