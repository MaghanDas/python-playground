
# Lists in Python
# A list is a mutable(changeable)collection of elements.
# defined using [] 
# can contains distinct type of elements.
courses=["programming", "Mathematics", "English", 23]
# print(type(courses))
# courses = {1,2,3}
# print(type(courses))

# print(courses[0])
# print(courses[-4]) # iprogramming
# negative indexing start in reversing order
# print(courses[-1]) # last element
# print(courses[0]) # first element.

# courses.append("Physics") # append in the last of the list
# print(courses.count("programming")) # prgramming appear once in list.
newlist = courses.copy() # copying the list from courses to newlist
# print(newlist)
# courses.clear() # clear the complete list.
# print(courses)
# courses.extend(newlist) # add newlist to the courses
dumy_list = [2,3,4,5]
dumy_list.extend(newlist)
# print(dumy_list)
# print(courses.index("programming")) 
num = [1,2,4,3]
num.sort() # sorting the num list.
# print(num)
# courses.reverse() # reverse the list...
# print(courses)
# courses.insert(1,"networking") # inserted at index 1, rest will be shifted ahead, nothing removes.
# print(courses)
# courses.remove("networking")
# print(courses.remove("networking")) # output -> none
# print(courses)

# Looping through list
# for course in courses:
#   print(course, end =", ")

# tuples in python
# a tuple is an immutable (unchangable) collection.
# tuples are defined using ().

# numbers = (1, 2, "hey", 4, 'a')

# print(numbers)
# print(numbers[0]) # first element
# print(numbers[-1]) # last element
# numbers[1] = 23 # error , because tuples are unchangeable..!

# person = ("Maghan", 23, "Student") # packing
# name, age, profession = person #unpacking
# print(person) # ('Maghan', 23, 'Student')
# print(name, age, profession) # Maghan 23 Student
# print(age)


#                      | List                                  |   Tuple
# -----------------------------------------------------------
# Mutable?      | ✅ Yes                             |  	❌ No
# Syntax           |	[ ]                                 |	  ( )
# Performance | Slower (More memory)   |    Faster (Less memory)
# Use Case	     | Dynamic collections       |	Fixed data


# evenNums = [2, 4, 6, 8, 10]
# print(evenNums)
# evenNums[1] = 100
# print(evenNums)

# numberTuple = tuple(evenNums) # conversion from list to tuple.
# numberList  = list(numberTuple) # conversion from tuple ot list.
# print(numberTuple)
# print(numberList)


# Create a list of 5 different numbers.
# Replace the third number in the list with a new number provided by the user.
# Create a tuple from the list.
# Print both the updated list and the tuple.
# Try to modify the tuple (this should result in an error since tuples are immutable).
# Print an error message when the modification attempt fails


# numbers = [1, 2, 3, 4, 5]
# numbers[2] = int(input("Enter a new number: "))  # Replace third element with user input
# tupleNum = tuple(numbers)  # Convert list to tuple

# print("Updated List:", numbers)
# print("Tuple:", tupleNum)

# try:
#     tupleNum[0] = 12  # Attempt to modify tuple (will raise an error)
# except TypeError as e:
#     print("Error: Can't modify tuple element!")  # Catch and handle the error




# 🔹 Quick Comparison Table
# Feature     	                 Lists   	        Tuples 	     Dictionaries	                  Sets
# Ordered?	                 ✅ Yes	    ✅ Yes  	  ✅ (Python 3.7+)	     ❌ No
# Mutable?	                ✅ Yes      	❌ No	 ✅ Yes                         ✅ Yes
# Allows Duplicates?  ✅ Yes	      ✅ Yes	   ❌No (keys)                ❌ No
# Key-Value Pairs?     ❌ No       ❌ No     ✅ Yes	                    ❌ No
# Indexing Allowed?	 ✅ Yes	     ✅ Yes    ❌No (Uses Keys)	  ❌ No



# Create a list of 5 different numbers.
# Replace the third number in the list with a new number provided by the user.
# Create a tuple from the list.
# Print both the updated list and the tuple.
# Try to modify the tuple (this should result in an error since tuples are immutable).
# Print an error message when the modification attempt fails

