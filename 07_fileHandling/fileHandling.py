
# 🔹 File Handling in Python 📂
# Python allows us to read from and write to files using built-in functions.

# ✅ Writing to a File
# ✅ "w" mode creates or overwrites a file.
# ✅ with open(...) automatically closes the file after writing.

with open("names.txt", "w") as file:
    file.write("Maghan")
    file.write("Das")


# ✅ Reading from a File
# ✅ "r" mode reads the file contents.

with open("names.txt","r") as file:
    content = file.read()
    print(content)

# 🔥 Mini Challenge
# Write a Python script to ask the user for their name and save it in a file called "user.txt".
# Read and print the saved name from "user.txt".

userName = input("enter your name")
with open("user.txt","w") as file:
    file.write(userName)

with open("user.txt", "r") as file:
    content = file.read()
    print("Saved name:", content)
