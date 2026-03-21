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