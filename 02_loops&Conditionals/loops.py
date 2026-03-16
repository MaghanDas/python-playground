
# for loop
# for i in range(5):
#     print("iteration: " ,i)
    
# for j in range(0,4,2):
#     print(j)

# while looop
# count = 0
# while count < 5:
#   print("count is: ", count)
#   count += 1

# looping through a list..
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#   print("I like: ",fruit)

# sum=0
# for i in range(5,10):
#   sum+=i
#   print(i,sum)
# print(sum)


# secret_number = 7

# while True: 
#     guess = int(input("enter an integer number:"))
#     if guess==secret_number:
#         break
#     print("Haahahah, not correct")

# print("GOOD JOB!!!")


# ─── LOOPS ─────────────────────────────────────────────
fruits = ["apple", "banana", "cherry"]

# Basic — rarely use this in Python
for i in range(len(fruits)):
    print(fruits[i])

# Pythonic — use this
for fruit in fruits:
    print(fruit)

# When you need the index too
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Looping two lists together
prices = [1.0, 2.0, 3.0]
for fruit, price in zip(fruits, prices):
    print(f"{fruit} costs ${price}")

# Dictionary loop
user = {"name": "Alice", "age": 25}
for key, value in user.items():
    print(f"{key}: {value}")

# ─── WHILE ─────────────────────────────────────────────
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    # simulate user input
    success = True
    if success:
        break
    attempts += 1
else:
    # while...else runs if loop completed WITHOUT break
    print("Max attempts reached")