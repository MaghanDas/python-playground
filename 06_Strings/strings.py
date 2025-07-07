
text = "A brown fox jumps over the lazy dog"
text2 =  "hello"
text3 = "G"
# print(text)
# print(text2)
# print(text3)

poem ='''Twinkle Twinkle little star,
How i wonder what you are'''

# print(poem)
# print(len(poem))
# print("star" in poem) # True

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.

character = "ABC"
# print(character[0]) # first 
# print(character[-1]) # last

#looping through sring character
# for x in character: 
#     print(x, end = " ")

txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
# print("expensive" not in txt)

# Slicing of a String.
b = "helloworld" 
# print(b[2:5])     # Get the characters from position 2 to position 5 (not included):
# print(b[:5]) # hello     , by default starts from 0
# print(len(b[5:])) # world
# Use negative indexes to start the slice from the end of the string:

# Modifing the strings.
text4 = "good Text "
# print(text4.capitalize() , text4.upper() , text4.lower(), text4.strip()) 
# Good text GOOD TEXT good text good Text
#  The strip() method removes any whitespace from the beginning or the end:

# print(text4.replace("T", "N")) # good Next 

# The split() method splits the string into substrings if it finds instances of the separator:
text5 = "Hello world"
# print(text5.split(" "))     # ['Hello', 'world']

a = "Hello"
b = "World"
c = a + b
# print(c)

# String formating: 
age = 23;
# print(f"My age is{age}")
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt) # The price is 59.00 dollars

# escape characters
print("I like \"stranger things\" show")
# print(23)
