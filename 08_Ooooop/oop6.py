
# Pillar - 4th OF OOP: Abstraction 

# users of our class don't need to know how it works.
# they just need to know what it does 

class DatabaseConnection:
    def __init__(self, host:str, port:int, db_name:str):
        self._host = host 
        self._port = port 
        self._db_name = db_name
        self._conn = None   # initial db state 
    
    def connect(self) -> None:
        self._conn = f"conn://{self._host}:{self._port}/{self._db_name}"
        print(f"Connected to {self._db_name}")

    def disconnect(self) -> None:
        self._conn = None 
        print("disconnected")

    def execute(self, query:str)-> list:
        if not self._conn:
            raise RuntimeError("Not connected: Call connect() first")

        print(f"Executing : {query}")
        return []
    # __enter__ and __exit__ make it a context manager (with statement)
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
        return False   # don't suppress exceptions

# # Caller doesn't care about internal connection logic
# withDatabaseConnection("localhost", 5432, "mydb") as db:
# db.execute("SELECT * FROM users")
# db.execute("SELECT * FROM orders")
# # disconnect() called automatically — even if exception occurs




# ======  Class Methods and Static Methods ===

class User:
    _user_count = 0 

    def __init__(self, name:str, email:str, role:str, str = "user"):
        self.name = name 
        self.email = email
        self.role = role 
        self._user_count += 1
    
    # ── @classmethod ─────────────────────────────────────────────
    # Receives the CLASS (cls) not the instance
    # Used as: alternative constructors, factory methods
    @classmethod
    def from_dic(cls,data:dict) -> "User":
        return cls(
            name = data["name"]
            email = data["email"]
            role = data.get("role", "user")
        )

    @classmethod
    def get_user_count(cls) -> int:
        return cls._user_count

    # ── @staticmethod ─────────────────────────────────────────────
    # No access to class or instance
    # Just a utility function that logically belongs here
    @staticmethod
    def is_valid_email(email: str) -> bool:
        return "@" in email and "." in email.split("@")[-1]

    def __repr__(self) -> str:
        return f"User(name={self.name!r}, role={self.role!r})"


# Using @classmethod as factory / alternative constructor
data = {"name": "Alice", "email": "alice@example.com", "role": "admin"}
alice = User.from_dict(data)

bob = User("Bob", "bob@example.com")

print(User.get_user_count())              # 2
print(User.is_valid_email("bad-email"))   # False
print(User.is_valid_email("a@b.com"))     # True
print(alice)                              # User(name='Alice', role='admin')
