

# ─── IF / ELIF / ELSE ──────────────────────────────────

age = 19

if age >= 18:
    print("You can vote")
else:
    print("you can not vote")


score = 85


if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# One-liner (ternary) — use only when it's truly simple
grade = "Pass" if score >= 60 else "Fail"
print(grade)


# TRUTHNESS--------------
# Falsy values: False, None, 0, 0.0m "", [], {}, set()
# everything else is truthy

name = ""
if not name:
    print("name is empty")
    
