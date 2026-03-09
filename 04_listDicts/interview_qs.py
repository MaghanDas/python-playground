# some interview questions on dictionaries 

# question:1: frequency counter 
nums = [1,1, 2,3,3,3,4]

freq={}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)
# explanation of the code:
#  freq[n] = freq.get(n, 0) + 1 what does it do?
# This line of code is used to count the frequency of each element in the list `nums
# # Here's how it works:
# 1. `freq.get(n, 0)`: This part of the code checks if the
# key `n` exists in the dictionary `freq`. If it does, it returns the current count of that key. If it doesn't exist, it returns `0` (the default value provided).    
# 2. `freq.get(n, 0) + 1`: This adds `1` to the current count of the key `n`. If the key doesn't exist, it effectively starts counting from `1` (since `0 + 1` equals `1`).
# 3. `freq[n] = ...`: This assigns the new count back to the key `n` in the dictionary `freq`. If the key already exists, it updates the count; if it doesn't exist, it creates a new key-value pair with the count of `1`.


