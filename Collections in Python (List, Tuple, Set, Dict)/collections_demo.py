# collections_demo.py

"""
This script demonstrates Python's core data structures:
- Lists
- Tuples
- Sets
- Dictionaries
- List & Dictionary Comprehensions
"""

# -------------------------------
# LIST DEMO
# -------------------------------
print("=== LIST DEMO ===")
fruits = ["apple", "banana", "cherry"]

# CRUD
fruits.append("mango")       # Create
print("After append:", fruits)

print("Read [1]:", fruits[1])  # Read

fruits[1] = "blueberry"      # Update
print("After update:", fruits)

del fruits[2]                # Delete
print("After delete:", fruits)

# Iteration
for fruit in fruits:
    print("Fruit:", fruit)


# -------------------------------
# TUPLE DEMO
# -------------------------------
print("\n=== TUPLE DEMO ===")
numbers = (10, 20, 30, 40)
print("Tuple:", numbers)

# Access
print("First element:", numbers[0])

# Tuples are immutable, so no update/delete allowed


# -------------------------------
# SET DEMO
# -------------------------------
print("\n=== SET DEMO ===")
colors = {"red", "green", "blue"}

# Add
colors.add("yellow")
print("After add:", colors)

# Remove
colors.remove("red")
print("After remove:", colors)

# Union & Intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)


# -------------------------------
# DICTIONARY DEMO
# -------------------------------
print("\n=== DICTIONARY DEMO ===")
student = {
    "name": "Alice",
    "age": 21,
    "course": "CS"
}

# CRUD
student["email"] = "alice@example.com"   # Create
print("After add:", student)

print("Read name:", student["name"])     # Read

student["age"] = 22                      # Update
print("After update:", student)

del student["course"]                    # Delete
print("After delete:", student)

# Iteration
for key, value in student.items():
    print(f"{key}: {value}")


# -------------------------------
# LIST COMPREHENSION
# -------------------------------
print("\n=== LIST COMPREHENSION ===")
nums = [1, 2, 3, 4, 5]
squares = [n**2 for n in nums]
print("Squares:", squares)

# Filtering
evens = [n for n in nums if n % 2 == 0]
print("Even numbers:", evens)


# -------------------------------
# DICTIONARY COMPREHENSION
# -------------------------------
print("\n=== DICTIONARY COMPREHENSION ===")
squares_dict = {n: n**2 for n in nums}
print("Squares dict:", squares_dict)

# Filtering
even_squares = {n: n**2 for n in nums if n % 2 == 0}
print("Even squares dict:", even_squares)

