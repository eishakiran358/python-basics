
# =====================Python Sets==========================
# ==========================================================
# 1. What is a Set?
# ==========================================================

"""
Definition:
A Set is an unordered, mutable collection
of unique elements. Duplicate values are
automatically removed.
"""

# ==========================================================
# 2. Why Use Sets?
# ==========================================================

"""
Advantages of Sets

1. Store unique values
2. Fast searching
3. Fast adding and removing
4. Supports mathematical set operations
5. Removes duplicate values automatically
"""

# ==========================================================
# 3. Creating a Set
# ==========================================================

print("========== Creating a Set ==========")

fruits = {"Apple", "Banana", "Mango"}

print(fruits)

print()

# ==========================================================
# 4. Set Data Types
# ==========================================================

print("========== Set Data Types ==========")

data = {10, 20.5, "Python", True}

print(data)

print()

# ==========================================================
# 5. Duplicate Values
# ==========================================================

print("========== Duplicate Values ==========")

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)

print("Duplicate values are removed automatically.")

print()

# ==========================================================
# 6. Access Set Items
# ==========================================================

print("========== Access Set Items ==========")

"""
Definition:
Sets do not support indexing.
Access items using a loop.
"""

fruits = {"Apple", "Banana", "Mango"}

for fruit in fruits:
    print(fruit)

print()

# ==========================================================
# 7. Loop Through a Set
# ==========================================================

print("========== Loop Through a Set ==========")

colors = {"Red", "Green", "Blue"}

for color in colors:
    print(color)

print()

# ==========================================================
# 8. Check Item Exists
# ==========================================================

print("========== Check Item Exists ==========")

fruits = {"Apple", "Banana", "Orange"}

if "Banana" in fruits:
    print("Banana Found")
else:
    print("Banana Not Found")

print()

# ==========================================================
# 9. Add Items
# ==========================================================

print("========== add() ==========")

fruits = {"Apple", "Banana"}

fruits.add("Mango")

print(fruits)

print()

print("========== update() ==========")

fruits.update({"Orange", "Grapes"})

print(fruits)

print()

# ==========================================================
# 10. Remove Items
# ==========================================================

print("========== remove() ==========")

numbers = {10, 20, 30, 40}

numbers.remove(20)

print(numbers)

print()

print("========== discard() ==========")

numbers.discard(30)

print(numbers)

print()

print("========== pop() ==========")

numbers.pop()

print(numbers)

print()

print("========== clear() ==========")

temp = {1, 2, 3}

temp.clear()

print(temp)

print()

print("========== del ==========")

colors = {"Red", "Green"}

print("Before Delete :", colors)

del colors

print("Set Deleted Successfully")

print()

# ==========================================================
# 11. Set Length
# ==========================================================

print("========== Set Length ==========")

numbers = {10, 20, 30, 40}

print("Length =", len(numbers))

print()

# ==========================================================
# 12. Join Sets
# ==========================================================

print("========== union() ==========")

set1 = {1, 2, 3}
set2 = {4, 5, 6}

result = set1.union(set2)

print(result)

print()

print("========== update() ==========")

set1 = {1, 2, 3}
set2 = {4, 5, 6}

set1.update(set2)

print(set1)

print()

# ==========================================================
# 13. Set Operations
# ==========================================================

print("========== intersection() ==========")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.intersection(B))

print()

print("========== intersection_update() ==========")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.intersection_update(B)

print(A)

print()

print("========== difference() ==========")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.difference(B))

print()

print("========== difference_update() ==========")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.difference_update(B)

print(A)

print()

print("========== symmetric_difference() ==========")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.symmetric_difference(B))

print()

# ==========================================================
# 14. Frozen Set (frozenset)
# ==========================================================

print("========== Frozen Set ==========")

numbers = frozenset({10, 20, 30, 40})

print(numbers)

print("Frozen Sets cannot be modified.")

print()

# ==========================================================
# 15. Set Methods
# ==========================================================

print("========== Set Methods ==========")

numbers = {10, 20, 30}

numbers.add(40)
print("add() :", numbers)

numbers.remove(20)
print("remove() :", numbers)

numbers.discard(100)
print("discard() :", numbers)

print()

# ==========================================================
# 16. Difference Between List, Tuple, Dictionary & Set
# ==========================================================

print("========== List vs Tuple vs Dictionary vs Set ==========")

print("List")
print("- Ordered")
print("- Mutable")
print("- Allows Duplicates")
print("- Uses []")

print()

print("Tuple")
print("- Ordered")
print("- Immutable")
print("- Allows Duplicates")
print("- Uses ()")

print()

print("Dictionary")
print("- Key-Value Pairs")
print("- Mutable")
print("- Keys Must Be Unique")
print("- Uses {}")

print()

print("Set")
print("- Unordered")
print("- Mutable")
print("- No Duplicate Values")
print("- Uses {}")

print()
