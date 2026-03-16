# to run the code..
# python3 filename

# print("Hello World!");

x = 10
print(x) # here's what actually happends under the hood.
''' 
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
'''
# Python is interpreted but also compiled — just compiled to bytecode, 
# not machine code. This is why Python is slower than C/Go but faster to write and run portably.

x = 10 # x points to integer objetc 10 in memory. 
y = x # y points to the same object, not a copy.

print(id(x)) # id() shows memory address 
print(id(y)) # same address, both points to the same object

y = 20 # Now y points to a new object (20)

# Everything in Python is an object. Integers, strings, functions, classes — all objects.
print(type(10))          # <class 'int'>
print(type("hello"))     # <class 'str'>
print(type(print))       # <class 'builtin_function_or_method'>
# Even None is an object
print(type(None))        # <class 'NoneType'>

age = 23;
name = "Raj";
# print(age);
# Age = str(age); # type casting from int to string
# print(type(age))
# print(type(Age)); # type() is used to check the type of the variable

# print("My name is " + name + " and my age is " + str(age));
# print(name + "12"); 
# in python only strings can be contenated , number by defauly are not typecasted to string like java. 
#  we have to do manulaylly typecasting.

# print(f"My name is {name} and my age is {Age}");
# print(name[0]); 

# isprogrammer, isdesigner = True, False;
# print(isprogrammer, isdesigner);

# name = input("Enter your name: ");
# print(f"Hello {name}");

# age,isPro,country = 23,True,"Hungary";
# print(age,isPro,country)

if age > 18:
  print("You are 18+");
elif age == 18:
  print("You are 18");
else:
  print(f"You are {age} years old");

# name=input()
# age = int(input("Enter your age: "));
# print(type(age))
# print(f"Hello {name}, you are {age} years old")

# Mutable vs Immutable in python:

# Immutable types: int, float, str, float, tuple 
# once created , the object cannot be chnaged.

name = "Alexx"
name.upper() # doesn't modfiy name 
print(name)
name = name.upper()  # Now name points to new object "ALICE"
print(name)          # "ALICE"


# Mutable types: list, dict, set . the object can be modified in place. 
nums = [2, 3, 4]
copy = nums # both points to the same list
copy.append(5) # modifies the object in place

print(nums) # also changed to : [2,3,4,5]
print(copy) # [2,3,4,5]


# ─── NUMBERS ───────────────────────────────────────────
age = 25                 # int  — no size limit in Python!
price = 19.99            # float — IEEE 754, has precision issues
from decimal import Decimal
price = Decimal("19.99") # Use this for money, never float

big = 10 ** 100          # Python ints handle arbitrary size
print(type(big))         # still <class 'int'>

# ─── STRINGS ───────────────────────────────────────────
name = "Alice"
multi = """
This is
multiline
"""
# f-strings (use these — fastest & most readable)
greeting = f"Hello, {name}. You are {age} years old."
greeting = f"Result: {2 + 2}"        # expressions work too
greeting = f"Upper: {name.upper()}"  # method calls work too

# ─── BOOLEANS ──────────────────────────────────────────
is_active = True
print(type(True))     # <class 'bool'>  — bool is subclass of int!
print(True + True)    # 2  ← this works (and is sometimes useful)
print(True == 1)      # True

# ─── NONE ──────────────────────────────────────────────
result = None
# Always check None with 'is', not ==
if result is None:        # CORRECT
    print("No result")
if result == None:        # works but not Pythonic — avoid
    print("No result")

# ─── LISTS ─────────────────────────────────────────────
items = [1, "hello", 3.14, True, None]  # mixed types allowed
items[0]       # first element
items[-1]      # last element
items[1:3]     # slice: ["hello", 3.14]
items[::-1]    # reverse

# ─── TUPLES ────────────────────────────────────────────
point = (10, 20)          # immutable list — use for fixed data
x, y = point              # unpacking
r, *rest = (1, 2, 3, 4)   # extended unpacking: r=1, rest=[2,3,4]

# ─── DICTIONARIES ──────────────────────────────────────
user = {
    "name": "Alice",
    "age": 25,
    "active": True
}
user["name"]              # "Alice"
user.get("email")         # None — safe, no KeyError
user.get("email", "N/A")  # "N/A" — default value

# ─── SETS ──────────────────────────────────────────────
tags = {"python", "backend", "python"}  # duplicates removed
print(tags)      # {"python", "backend"}

a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)     # intersection: {2, 3}
print(a | b)     # union: {1, 2, 3, 4}
print(a - b)     # difference: {1}
