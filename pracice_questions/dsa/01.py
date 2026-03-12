from collections import defaultdict

# questions : from list B elements find the position of the same element in list A:

n, m = map(int, input().split())

d = defaultdict(list)

# Store positions of words in group A
for i in range(1, n + 1):
    word = input()
    d[word].append(i)

# Process group B
for _ in range(m):
    word = input()

    if word in d:
        print(*d[word])
    else:
        print(-1)


# Question 2: 
# Given a list of shoe sizes and a list of customers with their desired shoe size and price they are willing to pay,
#  calculate the total sales. Each shoe can only be sold once.
from collections import Counter

x = int(input())
shoe_sizes = list(map(int, input().split()))
number_of_customers = int(input())

size_counter = Counter(shoe_sizes)

sales = 0

for _ in range(number_of_customers):
    size, price = map(int, input().split())

    if size_counter[size] > 0:
        sales += price
        size_counter[size] -= 1

print(sales)

# Question 3: Given a list of students with their names and scores, find the names of students with the second lowest score
#  and print them in alphabetical order.
if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # get unique sorted scores
    scores = sorted(set([s[1] for s in students]))
    second_lowest = scores[1]

    # get students with second lowest score
    names = [s[0] for s in students if s[1] == second_lowest]

    # print alphabetically
    for name in sorted(names):
        print(name)

        