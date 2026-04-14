# from basics of python to the advanced level. all in this one file.
x = 10
print(x)

"""
Your Code (.py file)
      ↓
  Lexer/Tokenizer        → breaks code into tokens
      ↓
  Parser                 → builds Abstract Syntax Tree (AST)
      ↓
  Compiler               → converts to Bytecode (.pyc)
      ↓
  Python Virtual Machine → executes bytecode line by line
      ↓
  Output
  """
# python practice
x = 10
y = x 

print(id(x))
print(id(y)) # points to same same object. same address as x
# print(type(y)) 

# everything in python is an object. integers, strings, functions, classes- all objects...

print(type(10))
print(type("Hello"))
print(type(print))
print(type(None))

print(" _______________________________________")

# Mutable vs immutable in python.
# immutable typesl int, float, tuple, bool. -> once create, the object cannot be changed

name = "Maghan"
name.upper() # doesn't modify name.
print(name) # still Maghan -> upper() returns new string.
print(name.upper())

# num = 10
# print(id(num)) # some address
# num += 10
# print(num)
# print(id(num)) # different than prev ones.

# Mutable types: list, dict, set.
# the objetc can be modified in place.

nums = [12,3, 4]
copy = nums # both points to same list
copy.append(4); # modifeies the object in list

print(nums,copy) # prints same.
# this is a problem here.  to avoid it.
real_copy = nums.copy(); # or list(nums), or nums[:]
real_copy.append(99);
print(nums, real_copy) # nums unchanged, real_copy got 99 appended.


# why this matters in production: passing mutable objetcs to functions can cause unexpected side effects - very common bug.



print(" _______ PYTHON DATA TYPES: _______________")

# print("_________ NUMBERSS __________")
age = 32 # int - no size limit in python
price = 19.19 # float , has precisoin issue.

from decimal import Decimal
price = Decimal("19.19") 
big = 10 ** 100 # python int handles arbitary size.
print(type(big))


# ____________STRINGS __________
name = "Asim"
# multi = """ This is a multime line """

# f-string(fastest- most readable)
greetings = f"Hello, {name}.  you are {age} years old"
addition = f"Result: {2+2}"
greeting_upper = f"Upper : {name.upper()}"

print(greetings)
print(addition)
print(greeting_upper)



# __________ BOOLEAN ____________
is_over_18 = True 
print(is_over_18)
print(type(is_over_18))
print(True + True)
print(False + False)
print(True - False)
print(True == 1) # true.



# ___________________ NONE ________
result = None 
if result is None:  # good correct way
    print("No result");
if result == None:
    print("Nor result") # not good style.


# _______________ LISTS _________

array = [1, "hello", 3.14, True, None] # mixed types allowed

print(array)
print(array[0]) # first element
print(array[-1]) # last element
print(array[1:3]) # slice ["hello", 3.14]
print(array[::-1]) # reverse



# _______________ TUPLES ____________
point = (10,20) # immutable list, used for fixed data.
x, y = point  # unpacking
r, *rest = (1,2,3,4) # extengind unpacking. r = 1, rest =[2,3,4]

# ____________ SETS _______
tags = {"python", "Backend", "python"}
print(tags) # duplicated not allowed. {"backend", "python"}

a = {1, 2, 3}
b = {2, 3, 4}

print(a & b) # intersection: {2,3}
print(a | b) # union: {1,2,3,4}
print(a - b) # difference = {1}


# ___________ CONTROL FLOW _________
print("__________ CONTROL FLOW_________")

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
    
grade = "pass" if score >= 60 else "Fail"

print(grade)

# ____ TRUTHINESS ________

# falsy values : False, None, 0, 0.0, "", [], {}, set()
# everything else is truthy

name = ""
if not name:
    print("Name is empty")

items = []
if not items:
    print("No items")

# ______________ LOOPS__________
print("________ LOOPS _____")

fruits = ['apple', 'banana','cheery']

# basic loop
for i in range(len(fruits)):
    print(fruits[i])

# pythonic loop - use this beter.
for fruit in fruits:
    print(fruit)

# when we need index as well
for i , fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# dictionary loop:
users = {
    "name": "Maghan",
    "Age": 22
}

for key , value in users.items():
    print(f"{key}: {value}")

# _________ WHILE ______
attemps = 0
max_attempts = 3

while attemps < max_attempts:
    success = True 
    if success:
        break
    attempts += 1
else:
    print("max attempts reached!")



# __________ FUCTIONS _______
print("________ FUNCTIONS_________")

# basic:
def greet(name):
    return f"hello, {name}"

# defualt arguements.
def greet(name, greeting = "hello"):
    return f"{greeting}, {name}"
    
    
print(greet("Das"))
print(greet("Das", "Hey"))
print(greet("Das", greeting="HI"))

# type hints - mostly used in production code.
def calculate_text(price: float, rate: float = 0.1)-> float:
    return price * rate
    
# multple return value. 
def min_max(numbers:list)->tuple[int, int]:
    return min(numbers), max(numbers)


low, high = min_max([2,1,3,4,5,9])

# *args and **kwargs 

def log(*args, **kwargs):
    print(args) # tuple of positinal arguements
    print(kwargs) # dict of keyword args
    
log("error", "something broke", "yes", level="ERROR", code=5000)
    

    
    
    



