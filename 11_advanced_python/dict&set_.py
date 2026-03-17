
# ─── DICT COMPREHENSION ────────────────────────────────────────
# Pattern: {key_expr: val_expr for item in iterable if condition}

names = ["Alice", "Bob", "Charlie"]
scores = [95, 82, 78]

# zip two list into a dictionary

grade_map = {name: score for name, score in zip(names, scores)}
print(grade_map) # {'Alice': 95, 'Bob': 82, 'Charlie': 78}

# invert a dictionary
inverted = {v:k for k, v in grade_map.items()}
print(inverted)

# filter a dictionary
passing = {k: v for k,v in grade_map.items() if v >= 80}
print(passing)

# transform values. 
normalized = {k: v/100 for k, v in grade_map.items()}
print(normalized)


# -------------- SET COMPREHENSION -------------
words = ["apple", "banana", "avocado", "blueberry", "cherry"]
starts = {w[0] for w in words} # unique first letters 
print(starts)
