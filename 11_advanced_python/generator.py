

numbers = range(1_000_000)

# List comprehension — creates entire list in memory (bad for huge data)
total = sum([n ** 2 for n in numbers])
print(total)

# Generator expression — computes one value at a time (memory efficient)
total = sum(n ** 2 for n in numbers)   # no square brackets!
print(total)

# Check the difference
import sys
list_comp = [n ** 2 for n in range(10000)]
gen_expr  = (n ** 2 for n in range(10000))

print(sys.getsizeof(list_comp))   # ~87,624 bytes
print(sys.getsizeof(gen_expr))    # 104 bytes  ← tiny!

# Use generators when you only need to iterate once
# Use lists when you need to index, slice, or reuse
