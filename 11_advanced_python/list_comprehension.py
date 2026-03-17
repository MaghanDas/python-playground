

# Pattern: [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Old way 
squares = []
for n in numbers:
    if n % 2 == 0:
        squares.append(n ** 2)

# with list comphrension 
squares = [n ** 2 for n in numbers if n % 2 == 0]
print(squares)

# some real-world examples 
names = [" aline", "  marley", "narey"]
clean = [name.strip().title() for name in names]
print(clean)


words = ['hello', 'world', 'python']
upper = [w.upper() for w in words if len(w) > 4]
print(upper)

# nested- flatten a 2d list
matrix = [[1,2,3], 
          [4,5,6],
          [7,8,9]]

flat = [num for row in matrix for num in row]
print(flat)

