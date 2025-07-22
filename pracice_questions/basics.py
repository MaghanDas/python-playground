# Python Basics
 
 # 01: Write a program to check if a number is even or odd.

# number = int(input("enter a number to check wether it's even or oddd: "))
# if number%2==0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# 02: Write a program to find the factorial of a given number using a loop.
# number =int( input("enter the number to check factorial for : "))
# fact = 1
# for i in range(1,number+1):
#     fact*=i

# print(f"factorial of {number} is {fact}")

# 03: Write a program to reverse a string without using built-in reverse functions.
name = input("enter a string to reverse: ")
for i in range(0,(name.__len__() ) // 2):
    temp=i
    i=name[(name.__len__())-1]
    name[(name.__len__() )-1] = i

print(name)

# Write a program to count the number of vowels in a given string.
# Write a program to print the Fibonacci series up to n terms.
# Write a program to check if a given string is a palindrome.
# Write a program to find the largest and smallest elements in a list.
# Write a program to remove duplicates from a list.
# Write a program to merge two dictionaries.
# Write a program to check if a number is prime.