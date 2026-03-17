
# The 4 Pillars of OOP..

# Pillar - 1 : Encapsulation (hiding/encapsulation of the data)

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0):
        self.owner = owner
        self._balance = initial_balance    # _  = "private by convention"
        self.__ledger = []                 # __ = name-mangled (harder to access)

    # Property — access like attribute, works like a method
    @property
    def balance(self) -> float:
        return self._balance

    # Setter — validate before allowing change
    @balance.setter
    def balance(self, amount: float):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        self.__ledger.append(f"Deposit: +{amount}")

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self.__ledger.append(f"Withdrawal: -{amount}")

    def get_history(self) -> list:
        return self.__ledger.copy()   # return copy, not original


account = BankAccount("Alice", 1000)

# Clean interface — no direct mutation
account.deposit(500)
account.withdraw(200)
print(account.balance)        # 1300  ← via @property, looks like attribute

# account._balance = -999   # possible but violates convention
# account.__ledger          # AttributeError — name mangled to _BankAccount__ledger

print(account.get_history())
# ['Deposit: +500', 'Withdrawal: -200']

# Pillar -2 : Inheritance 
class Animal:
    def __init__(self, name:str, sound: str):
        self.name = name
        self.sound = sound

    def speak(self)-> str:
        return f"{self.name} says {self.sound}"

    def __repr__(self)-> str:
        return f"{self.__class__.__name__}(name={self.name!r}, sound={self.sound!r})"
    
class Dog(Animal):
    def __init__(self, name:str, breed: str):
        super().__init__(name, "Woof")
        self.breed = breed 
    
    def fetch(self)-> str:
        return f"{self.name} is fetching a ball." 

class Cat(Animal):
    def __init__(self, name:str, breed: str):
        super().__init__(name, "Meow")
        self.breed = breed 
    
    def speak(self)-> str:
        base = super().speak()
        return f"{base} - Purr Purr"

dog = Dog("Rex", "German Shepherd")
cat = Cat("Whiskers", "Siamese")

print(dog.speak())    # Rex says Woof          ← inherited from Animal
print(dog.fetch())    # Rex fetches the ball!  ← Dog-specific
print(cat.speak())    # Whiskers says Meow (and ignores you)  ← overridden

# isinstance checks — very useful in production
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True  ← Dog IS an Animal
print(isinstance(cat, Dog))     # Fals
print(isinstance(cat, Animal))  # True  ← Cat IS an Animal
