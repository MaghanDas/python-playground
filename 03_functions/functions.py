
# 🔹 What is a Function?
# A function is a block of reusable code that performs a specific task.
#  It helps in making the code modular, reusable, and organized.

# 🔹 Defining a Function
# We use the def keyword to define a function

# def fun():
#   print("Hello function")

# def fun(name):
#     print(f"Hello {name}")


# fun()
# fun("das")

def sum(a, b):
    return (a+b)

def nums(*num):
    print(num[1])

# print(sum(3, 2));
# nums(1, 2, 3, 4, 5, 6);


# range(start, stop, step)
# start (optional) → The starting number (default is 0).
# stop (required) → The number where the sequence stops (exclusive).
# step (optional) → The difference between consecutive numbers (default is 1).

# factorial of a numebr!!
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i      
    return fact

def factorial2(num):
    if num == 0:
        return 1
    else:
            return num*factorial2(num-1);
# print(factorial(4))
# print(factorial2(4))
# print(factorial(0))


# for i in range(0,100,2):
    # print(i)
    # print(i, end=",") 
    # print(i, end=" ") 

# print(1, 2, 3, 4, 5, sep=", ")
# print("H", "E", "L", "L", "O", sep="")


# 🔥 Mini Challenge
# Create a function called multiply that takes two numbers and returns their product.
# Create a function called is_even that takes a number and returns True if even, else False.
# Modify is_even to return a custom message instead of True/False.

def multiply(num1, num2):
    return num1*num2

def is_even(num):
    if num%2==0:
        # return True
        return "is even"
    else:
        # return False
        return "not even"

# print(multiply(2,3))
# print(is_even(3))

# Ternary operator 
def is_even2(num):
    return "is even" if num%2==0 else "not even"

# print(is_even2(3))

# 🔹 Lambda Functions
# Python allows anonymous functions using the lambda keyword

# square = lambda x: x * x 
# multiply = lambda x,y: x*y
# print(square (5))
# # print(multiply(3,4))

# 🔹 Recursion in Python
#  A function that calls itself is called a recursive function. It is useful for problems like factorial, Fibonacci, tree traversal, etc.

# factorial using recursion

def factRec(num):
    if num == 0 or num==1: # base case 
        return 1
    else:
        return num*factRec(num-1)
    
# print(factRec(0))

# 🔥 Mini Challenge
# Write a recursive function to calculate the sum of digits of a number.
# Write a recursive function to calculate Fibonacci numbers.


def sumDigits(num):
    if num == 0:
        return 0
    else:
        return num%10 + sumDigits(num // 10) # // floor division, rounds to num to nearest whole number...

# print(sumDigits(23))
# print(sumDigits(2334))
# print(sumDigits(100))
# print(sumDigits(1))

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(4))

# ✅ Base cases: fibonacci(1) = 0, fibonacci(2) = 1.
# ✅ Recursive step: F(n) = F(n-1) + F(n-2).
# ✅ Output for fibonacci(4): 2 (✅ Correct: 0, 1, 1, 2).


# some more function knowledge :  used in production

def calculate_tax(price: float, rate: float = 0.1) -> float:
    return price * rate 

# multiple return values: returns a tuple
def min_max(numbers: list) -> tuple[int, int]:
    return min(numbers), max(numbers)

low, high = min_max([1,2,3,5,2,6,7])

# *args and **kwargs 
def log(*args, **kwargs):
    print(args) # tuple of positional args
    print(kwargs) # dict of keyword args

log("error", "something broke", level="ERROR", code=500)
# ('error', 'something broke')
# {'level': 'ERROR', 'code': 500}


# exercise:
# 1. What does this print and WHY?
a = [1, 2, 3]
b = a
b += [4]
print(a)

# 2. Fix this function so it doesn't mutate the input
def add_default(data: dict, key: str, value) -> dict:
    data[key] = value
    return data

# 3. Write a function that takes any number of numbers
# and returns their average. Handle empty input gracefully.

# 4. What's the output?
print(bool(0), bool(""), bool([]), bool(None))
print(bool(1), bool("a"), bool([0]), bool(False))