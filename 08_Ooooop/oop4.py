
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