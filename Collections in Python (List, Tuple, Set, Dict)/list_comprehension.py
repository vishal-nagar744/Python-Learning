# ✅ 1. List Comprehension

# List comprehension provides a concise way to create lists in Python.

# 🔹 Basic Syntax:
# [expression for item in iterable if condition]


# 🔹 Examples:

# Square of numbers (1 to 5):

squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]


# Even numbers from 1 to 10:

print("Even Numbers:")   # Heading print hogi
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]


# First letter of each word:

words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]
print(first_letters)  # ['a', 'b', 'c']



# ✅ 2. Dictionary Comprehension
# Just like lists, we can build dictionaries in one line.

# Basic Syntax:
# {key_expression: value_expression for item in iterable if condition}


# 🔹 Examples:

# Number and its square (1 to 5):

squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Filter dictionary (only items with value > 2): 

numbers = {"a": 1, "b": 2, "c": 3, "d": 4}

filtered = {}   # सबसे पहले खाली dictionary बनाते हैं

for k, v in numbers.items():   # हर key और value पर loop लगाते हैं
    if v > 2:                  # condition check करते हैं
        filtered[k] = v        # condition true होने पर entry add करते हैं

print(filtered)  # {'c': 3, 'd': 4}


# Create dictionary from list of words (word: length):

words = ["apple", "banana", "cherry"]
lengths = {word: len(word) for word in words}
print(lengths)  # {'apple': 5, 'banana': 6, 'cherry': 6}
