
from importlib.resources import path
from pathlib import Path 

base = Path("data")
file =  base / "users" / "file.json" # / operator builds paths 

print(file)
print(file.name)
print(file.stem)
print(file.suffix)
print(file.parent)


# common operations 
file.parent.mkdir(parents=True, exist_ok=True) # create parent directories if they don't exist
print(file.exists()) # check if file exists
file.touch() # create an empty file if it doesn't exist


# Read/write directly via path 
Path(notes.txt).write_text("This is a note.") # write text to file
content = Path(notes.txt).read_text() # read text from file
print(content)

# list all fiels in a directory 
for f in Path(".").iterdir():
    print(f)

# find all python files recursively
for f in path(".").rglob("*.py"):
    print(f)