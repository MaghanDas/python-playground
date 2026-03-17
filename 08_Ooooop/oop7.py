# production patterns : Dataclasses (Modern python)
# Writing __init__, __repr__, __eq__ manually is tedious.
# dataclasses generate them automatically.

from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Product:
    name:        str
    price:       float
    category:    str
    in_stock:    bool  = True
    tags:        list  = field(default_factory=list)  # mutable default — ALWAYS use field()
    created_at:  datetime = field(default_factory=datetime.now)

    def apply_discount(self, percent: float) -> "Product":
        from dataclasses import replace
        new_price = self.price * (1 - percent / 100)
        return replace(self, price=round(new_price, 2))  # returns new object

    def __post_init__(self):
        # Runs after __init__ — good for validation
        if self.price < 0:
            raise ValueError(f"Price cannot be negative: {self.price}")


p1 = Product("Laptop", 999.99, "Electronics", tags=["tech", "work"])
p2 = Product("Phone",  599.99, "Electronics")

# print(p1)
# Product(name='Laptop', price=999.99, category='Electronics', ...)

discounted = p1.apply_discount(10)
# print(discounted.price)   # 899.99
# print(p1.price)           # 999.99 ← original unchanged

# __eq__ auto-generated
p3 = Product("Laptop", 999.99, "Electronics", tags=["tech", "work"])
# print(p1 == p3)    # True  ← compares all fields

# ConceptWhen to Use__init__Initialize instance state@propertyControlled attribute access with validationsuper()Call parent class methods in inheritanceABC + @abstractmethodDefine contracts — force child classes to implement@classmethodFactory methods, alternative constructors@staticmethodUtility functions that belong to the class logicallyDunder methodsMake objects work with Python operators and builtins@dataclassSimple data-holding classes — less boilerplate



# Task:
# 1. Build an Employee class hierarchy:

class Employee:
    def __init__(self, name:str, salary: int):
        self.name = name 
        self.salary = salary 
    
    def give_raise(self, percent: float) -> float:
        if percent < 0:
            raise ValueError("Raise percentage cannot be negative")
        self.salary += self.salary * (percent / 100)
        return self.salary

#  - Base: Employee(name, salary)
#    - Child: Manager(name, salary, team_size)

class Manager(Employee):
    def __init__(self, name:str, salary: int, language: str):
        self.name = name 
        self.salary = salary 
        self.language = language 
    
#    - Child: Developer(name, salary, language)
class Developer(Employee):
    def __init__(self, name:str, salary: int, language: str):
        self.name = name 
        self.salary = salary 
        self.language = language 

#    - Override __repr__ on each

# 2. Add a @classmethod `from_csv_row` to Employee
#    that takes "Alice,90000" and returns an Employee

# 3. Create a ShoppingCart class that:
#    - Stores list of Products (from dataclass above)
#    - Has add_item(), remove_item(), total() methods
#    - total() applies discount if cart > $500
#    - Supports len(cart) and str(cart)

# 4. What's the output and WHY?
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
c = Counter()
print(Counter.count)
print(a.count)