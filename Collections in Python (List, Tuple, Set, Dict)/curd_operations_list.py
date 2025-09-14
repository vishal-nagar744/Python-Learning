# 1) CREATE (Add/Insert Elements)

fruits = ["apple", "banana"]

# append() → end me add karega
fruits.append("mango")
print(fruits)  # Output: ['apple', 'banana', 'mango']

# insert(index, value) → specific position pe add karega
fruits.insert(1, "orange")
print(fruits)  
# ['apple', 'orange', 'banana', 'mango']

# extend() → ek list ke sare elements dusri list me add
fruits.extend(["grapes", "pineapple"])
print(fruits)  
# ['apple', 'orange', 'banana', 'mango', 'grapes', 'pineapple']


# 2) READ (Access Elements)

fruits = ["apple", "banana", "mango", "grapes"]

# index se access
print(fruits[0])   # apple
print(fruits[2])   # mango

# negative index
print(fruits[-1])  # grapes
print(fruits[-2])  # mango

# slicing
print(fruits[1:3])  # ['banana', 'mango']
print(fruits[:2])   # ['apple', 'banana']
print(fruits[2:])   # ['mango', 'grapes']


# 3) UPDATE (Modify Elements)

fruits = ["apple", "banana", "mango"]

# ek element update
fruits[1] = "orange"
print(fruits)  
# ['apple', 'orange', 'mango']

# multiple elements update
fruits[0:2] = ["kiwi", "papaya"]
print(fruits)  
# ['kiwi', 'papaya', 'mango']


# 4) DELETE (Remove Elements)

fruits = ["apple", "banana", "mango", "grapes"]

# remove() → value se delete
fruits.remove("banana")
print(fruits)  
# ['apple', 'mango', 'grapes']

# pop(index) → index se delete karega (default last)
fruits.pop()
print(fruits)  
# ['apple', 'mango']

fruits.pop(0)
print(fruits)  
# ['mango']

# del → index ya pura list delete
fruits = ["apple", "banana", "mango"]
del fruits[1]
print(fruits)  
# ['apple', 'mango']

# clear() → puri list empty kar dega
fruits.clear()
print(fruits)  
# []



# 🟣 Extra Useful Methods

fruits = ["apple", "banana", "mango", "banana"]

print(len(fruits))       # length
print(fruits.count("banana"))  # 2 times banana
print(fruits.index("mango"))   # 2

fruits.sort()  
print(fruits)  # alphabetically sort karega

fruits.reverse()  
print(fruits)  # reverse order
