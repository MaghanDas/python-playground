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
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return reverse_string(s[1:]) + s[0]

# name = input("Enter a string to reverse: ")
# print("Reversed string:", reverse_string(name))

# name = input("Enter a string to reverse: ")
# print("Reversed string:", name[::-1])

# print(name)

# Write a program to count the number of vowels in a given string.
# word = input("enter the word to count vowels for: ")
# vowel = "aeiou"
# count=0
# for i in word:
#     if i in vowel:
#         count += 1

# print(count)

# Write a program to print the Fibonacci series up to n terms.
# n = int(input("enter the number : "))
# a=0
# b=1
# print(a , " " , b , end=" " ) 
# for i in range(n-2):
#     next = a + b 
#     print(next , end=" ")
#     a = b
#     b= next
    
# Write a program to check if a given string is a palindrome.
# string = input("Enter a string to check palindrome: ")

# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# string = input("Enter a string to check palindrome: ")
# is_palindrome = True

# for i in range(len(string) // 2):
#     if string[i] != string[-(i + 1)]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# Finding maximum and minimum in the list.
# nums = [1, 2, 3, 7, 4, 5, 6]
# Initialize max and min with the first element
# maximum = nums[0]
# minimum = nums[0]
# for num in nums:
#     if num > maximum:
#         maximum = num
#     if num < minimum:
#         minimum = num

# print("Max in list is:", maximum)
# print("Min in list is:", minimum)

# # Write a program to remove duplicates from a list.
# nums = [1,2,2,3,4,2,2,5]
# nums = list(set(nums))
# print(nums)

# nums = [1, 2, 2, 3, 4, 2, 2, 5]
# unique_nums = []

# for num in nums:
#     if num not in unique_nums:
#         unique_nums.append(num)

# print(unique_nums)  # Output: [1, 2, 3, 4, 5]

# nums = [1, 2, 2, 3, 4, 2, 2, 5]
# nums = list(dict.fromkeys(nums))
# print(nums)  # Output: [1, 2, 3, 4, 5]

# Write a program to merge two dictionaries.
dictionary1 = {
   "name" : "das",
    "age": 13,
    "major": "computer science"
}
dictionary2 = {
    "nationality" : "pakistani"
}
# merged = dictionary1 | dictionary2
# print(merged)
# dictionary1.update(dictionary2)
# print(dictionary1)  # dictionary1 is now merged in-place
# merged = {**dictionary1, **dictionary2}
# print(merged)

# Write a program to check if a number is prime
count = 0
num = int (input("Enter the num to check for : "))

for i in range(1,num+1):
    if num % i == 0:
        count +=  1

if count==2:
    print(f"{num} is prime")
else:
    print(f"{num} is not a prime")