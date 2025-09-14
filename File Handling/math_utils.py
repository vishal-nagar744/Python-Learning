# 📌 1. What is a Module?
# 👉 A module is simply a Python file (.py) that contains variables, functions, or classes.
# It helps us organize code and reuse it across multiple files.
# Example (math_utils.py):

# math_utils.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b



# 📌 2. Built-in Modules
# Python already provides many modules. Example:

import math
import random
import datetime

print(math.sqrt(16))      # 4.0
print(random.randint(1, 10))   # Random number
print(datetime.datetime.now()) # Current date-time