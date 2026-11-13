
# Stage 1 — Python Core Mastery
# Starting here

# Writing Python naturally and understanding what happens underneath.
# - Functions, scope, closures
# - Mutable vs immutable objects
# - References, identity, copying
# - Dictionaries, sets, lists, tuples
# - Comprehensions and unpacking
# - Exceptions and error handling
# - Iterators, generators, decorators
# - Context managers
# - Modules, packages, typing
  
#   Stage 2 — Advanced Python
# - OOP, inheritance, composition
# - Dunder methods and data model
# - Memory management and garbage collection
# - Concurrency, threading, multiprocessing
# - Asyncio and asynchronous programming
# - Profiling and optimization
  
#   Stage 3 — Data Structures & Algorithms
# - Arrays and strings
# - Hash maps and sets
# - Two pointers
# - Sliding window
# - Stack and queue
# - Linked lists
# - Binary search
# - Trees and binary search trees
# - Heaps and priority queues
# - Graphs and graph traversal
# - Backtracking
# - Dynamic programming
  
#   Stage 4 — Problem-Solving Mastery
# - Recognizing patterns
# - Analyzing time and space complexity
# - Optimizing brute-force solutions
# - Handling edge cases
# - Writing solutions under interview time constraints
# - Explaining your approach clearly
  
#   Stage 5 — Professional Python Engineering
# - Clean architecture
# - SOLID principles
# - Type hints and static checking
# - Pytest and unit testing
# - Logging and debugging
# - Design patterns
# - REST APIs with FastAPI
# - SQL and database integration
# - Git, packaging and deployment
  
#   Stage 6 — Real-World Projects & Interviews
# - Build production-style Python applications
# - Refactor poorly written code
# - Debug unfamiliar codebases
# - Python-specific interview questions
# - LeetCode medium/hard practice
# - Mock technical interviews


# It should accept a list of integers and return a dictionary containing:
# 1. The minimum number.
# 2. The maximum number.
# 3. The sum of all numbers.
# 4. The average.
# 5. The number of even numbers.
# 6. The number of odd numbers.

def analyze_numbers(numbers):
  if len(numbers) == 0:
    print("Empty List! Pleease give a good list.")
    return {}
  solution = {}
#  Min, Max, Sum, AVG, COUNT(EVENS), COUNT(ODDS)
  maximum = numbers[0]
  minimum = numbers[0]
  total = 0
  even_count = 0
  odd_count = 0
  
  for num in numbers:
    total += num 
    if num > maximum:
      maximum = num
    if num < minimum:
      minimum = num
    if num % 2 == 0:
      even_count += 1
    if num % 2 != 0:
      odd_count += 1
      
  solution['maximum'] = maximum
  solution['minimum'] = minimum
  solution['sum'] = total
  solution['average'] = total / len(numbers)
  solution['even_count'] = even_count
  solution['odd_count'] = odd_count
  
  
  return solution

print(analyze_numbers([1, 2, 3, 4, 5]))
print(analyze_numbers([-10, -5, 0, 5, 10]))
print(analyze_numbers([7]))
print(analyze_numbers([]))


def second_largest(numbers):
    if len(numbers) < 2:
        return None

    maximum = None
    second_max = None

    for num in numbers:

        if maximum is None or num > maximum:
            second_max = maximum
            maximum = num

        elif num != maximum and (
            second_max is None or num > second_max
        ):
            second_max = num

    return second_max


print(second_largest([10, 5, 20, 8, 15]))  # 15
print(second_largest([10, 10, 8, 8]))      # 8
print(second_largest([5, 5, 5]))           # None
print(second_largest([-5, -2, -10]))       # -5
print(second_largest([7]))                 # None
print(second_largest([]))                 # None
