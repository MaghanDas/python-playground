
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


secret_number = 7

while True: 
    guess = int(input("enter an integer number:"))
    if guess==secret_number:
        break
    print("Haahahah, not correct")

print("GOOD JOB!!!")