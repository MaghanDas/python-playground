from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/subtract/{a}/{b}")
def subtract(a: int, b: int):
    return {"result": a - b}

@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    return {"result": a * b}

@app.get("/divide/{a}/{b}")
def divide(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero is not allowed."}
    return {"result": a / b}

@app.get("/fibonacci/{n}")
def fibonacci(n: int):
    if n < 0:
        return {"error": "Input must be a non-negative integer."}
    elif n == 0:
        return {"result": 0}
    elif n == 1:
        return {"result": 1}
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return {"result": b}

@app.get("/factorial/{n}")
def factorial(n: int):
    if n < 0:
        return {"error": "Input must be a non-negative integer."}
    elif n == 0 or n == 1:
        return {"result": 1}
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return {"result": result}

