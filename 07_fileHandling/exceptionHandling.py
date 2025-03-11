

# 🔹  Exception Handling
# Exception handling allows us to handle errors gracefully without crashing the program.

# ✅ Try-Except Block

# try:
#     num = int(input("enter number : "))
#     print(f"you entered {num}")
# except ValueError:
#     print("Nope! that's not the correct num.")

try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter first number: "))
    print("Division is ", num1 // num2)
except ValueError:
       print("Nope! that's not the correct num.")
except ZeroDivisionError:
      print("Eror! can't divide by zero")
    
