# 🟢 Python List Kya Hai?
# List ek ordered collection hai jisme multiple items store kar sakte ho.
# Items alag-alag types ke ho sakte hain (int, float, string, bool, etc.)
# List mutable hoti hai (yaani change kar sakte ho).
# List ko [] (square brackets) me likhte hain.

# Example:

# fruits = ["apple", "banana", "mango"]
# numbers = [10, 20, 30, 40]
# mixed = [1, "hello", 3.5, True]





# Example with List

# Basic Slice
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[1:4])   # Output: [20, 30, 40]


# Omit Start
print(numbers[:3])   # Output: [10, 20, 30]


# Omit End
print(numbers[3:])   # Output: [40, 50, 60, 70]


# Step ka use
print(numbers[::2])   # Output: [10, 30, 50, 70]


# Reverse List 
print(numbers[::-1])  # Output: [70, 60, 50, 40, 30, 20, 10]


# 1 → start index (matlab index 1 se shuru karo = 20)
# 6 → stop index (index 6 tak jao, lekin 6 include nahi hoga → 70 nahi aayega)
# 2 → step (matlab ek element lene ke baad 1 element skip karo)

# Middle with Step
print(numbers[1:6:2])  # Output: [20, 40, 60]


# 🔹 Example with Tuple

# Tuple bhi list ki tarah hi hota hai, bas immutable hota hai (change nahi kar sakte).

fruits = ("apple", "banana", "cherry", "mango", "orange")
print(fruits[1:4])  # Output: ('banana', 'cherry', 'mango')

# Omit Start
print(fruits[:3])   # Output: ('apple', 'banana', 'cherry')

# Omit End
print(fruits[2:])   # Output: ('cherry', 'mango', 'orange')


# step 
print(fruits[::2])  # Output: ('apple', 'cherry', 'orange')


# Reverse
print(fruits[::-1]) # Output: ('orange', 'mango', 'cherry', 'banana', 'apple')


