# 1. String Operations

# String banana
text = "Python"

# Concatenation (jodna)
print("Hello " + text)       # Hello Python

# Repetition (bar-bar repeat)
print(text * 3)              # PythonPythonPython

# Length
print(len(text))             # 6

# Indexing (0 se start hota hai)
print(text[0])   # 'P'
print(text[5])   # 'n'

# Slicing
print(text[0:4])   # 'Pyth' (index 0 to 3)
print(text[::-1])  # 'nohtyP' (reverse string)

# Membership test
print("Py" in text)    # True
print("Java" in text)  # False


# 2. Number Operations

a = 10
b = 3

# Addition
print(a + b)   # 13

# Subtraction
print(a - b)   # 7

# Multiplication
print(a * b)   # 30

# Division (float result)
print(a / b)   # 3.333...

# Integer Division (quotient only)
print(a // b)  # 3

# Modulus (remainder)
print(a % b)   # 1

# Power
print(a ** b)  # 1000 (10^3)



# 3. Mixing Strings & Numbers

a = 10
b = 3

# Addition
print(a + b)   # 13

# Subtraction
print(a - b)   # 7

# Multiplication
print(a * b)   # 30

# Division (float result)
print(a / b)   # 3.333...

# Integer Division (quotient only)
print(a // b)  # 3

# Modulus (remainder)
print(a % b)   # 1

# Power
print(a ** b)  # 1000 (10^3)



# 4. Small Practice

# 1. Concatenate two strings
first = "Hello"
second = "World"
print(first + " " + second)   # Hello World

# 2. Repeat string
print("Hi! " * 3)   # Hi! Hi! Hi!

# 3. Do some math
x = 7
y = 2
print("x+y =", x+y)
print("x-y =", x-y)
print("x*y =", x*y)
print("x/y =", x/y)
print("x%y =", x%y)