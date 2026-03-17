
import csv 

# ----------- write CSV file -----------

employees = [
    {"name": "Alice", "age": 30, "department": "HR"},
    {"name": "Bob", "age": 25, "department": "IT"},
    {"name": "Charlie", "age": 35, "department": "Finance"}
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "department"])
    writer.writeheader()  # write column names
    writer.writerows(employees)  # write multiple rows


# READ CSV file

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # each row is a dictionary