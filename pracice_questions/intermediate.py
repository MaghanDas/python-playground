# Write a function that accepts any number of arguments and returns their sum.
# def getSum(*nums):
#     sum=0
#     for i in range(len(nums)):
#         sum += nums[i]
        
#     return sum

# print(getSum(0,1,2,3,4,5,6))

# Write a program to sort a list of dictionaries by a key.
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

people_sorted = sorted(people, key=lambda dic: dic["age"])
# print(people_sorted)

# Write a program to read a text file and count the frequency of each word.


# Write a program to generate a list of squares of numbers from 1 to 20 using list comprehension.
squares = [x**2 for x in range(1, 21)]
print(squares)

# Write a function to check if two strings are anagrams.

# Write a program to find the common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = list(set(list1) & set(list2))
print(common_elements)

# Write a function to find the nth Fibonacci number using recursion.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(10))


# Write a program to flatten a nested list.
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

# Write a function that uses *args and **kwargs.
def print_values(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Write a program to implement a simple calculator using functions.
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# more dsa questions to practice 

    
