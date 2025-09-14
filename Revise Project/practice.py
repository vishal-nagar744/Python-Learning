
# 🔹 Variables
# Variables = data ko store karne ke liye naam

x = 10        # integer
name = "Honey"  # string
pi = 3.14     # float
is_active = True  # boolean



# 🔹 Strings
# Strings = text data
# Useful operations:

s = "Python"
print(s.upper())     # "PYTHON"
print(s.lower())     # "python"
print(s[0])          # "P" (indexing)
print(s[1:4])        # "yth" (slicing)
print(len(s))        # 6


# 🔹 Collections
# List (ordered, mutable)

fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits[1])   # banana


# Set (unordered, unique values)
nums = {1, 2, 3, 3, 4}
print(nums)  # {1, 2, 3, 4}


# Dictionary (key-value pairs)
student = {"name": "Honey", "age": 21}
print(student["name"])  # Honey



# 🔹 Conditions
age = 18
if age >= 18:
    print("You can vote")
elif age == 17:
    print("Almost there")
else:
    print("Too young")



# 🔹 Loops
# For loop
for i in range(5):
    print(i)

# While loop
count = 3
while count > 0:
    print(count)
    count -= 1


#  🔹 Functions
# simple function
def greet(name):
    return f"Hello {name}!"

print(greet("Honey"))