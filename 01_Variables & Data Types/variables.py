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