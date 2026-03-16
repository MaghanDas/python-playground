

# ----------- TRY / EXCEPT ---------------

try:
    a = 12
    print(a)
    result = 10 / 0 # error occurs..
except ZeroDivisionError:
    print("Cannot divide by zero")

# catching multiple exception
try:
    data = int("abc")
except (ValueError, TypeError) as e:
    print(f"Conversion error: {e}")



# The full Structure:
try:
    file = open("data.txt")
    content = file.read()
except FileNotFoundError as e:
    print(f"File not found: {e}")
except PermissionError as e:
    print(f"Permission error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}") # catch-all -use sparingly
else:
    # Runs only if no exception occurs
    print(f"Read {len(content) } characters")
finally:
    # Always runs - expcetions or not
    # use for cleanup - close files: DB connectionns etc
    print("Done.")


### Python's Exception Hierarchy — Know This for Interviews
'''
BaseException
├── SystemExit              ← sys.exit()
├── KeyboardInterrupt       ← Ctrl+C
└── Exception               ← catch this, not BaseException
    ├── ValueError          ← wrong value type ("abc" → int)
    ├── TypeError           ← wrong type entirely
    ├── KeyError            ← dict key doesn't exist
    ├── IndexError          ← list index out of range
    ├── AttributeError      ← object has no attribute
    ├── FileNotFoundError   ← file doesn't exist
    ├── ZeroDivisionError
    ├── RuntimeError
    └── 
'''