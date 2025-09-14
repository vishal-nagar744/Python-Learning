# text = "apple,banana,orange,grapes"

# # Split by comma
# fruits = text.split(",")
# print(fruits)   # ['apple', 'banana', 'orange', 'grapes']

# # Split by default (space)
# sentence = "Hello world Python is fun"
# words = sentence.split()
# print(words)   # ['Hello', 'world', 'Python', 'is', 'fun']


# fruits = ['apple', 'banana', 'orange', 'grapes']

# # Join with comma
# joined = ",".join(fruits)
# print(joined)   # "apple,banana,orange,grapes"

# # Join with space
# sentence = " ".join(fruits)
# print(sentence)  # "apple banana orange grapes"



# name = "Vishal"
# age = 21

# # f-string
# print(f"My name is {name} and I am {age} years old.")

# # You can even do calculations inside
# print(f"In 5 years, I will be {age + 5} years old.")




# name = "Vishal"
# age = 21

# # Basic usage
# print("My name is {} and I am {} years old.".format(name, age))

# # Positional formatting
# print("My name is {0} and I am {1} years old.".format(name, age))

# # Named placeholders
# print("My name is {n} and I am {a} years old.".format(n=name, a=age))


# int → str

# num = 100
# num_str = str(num)
# print(num_str, type(num_str))   # "100" <class 'str'>

# # str → int
# text = "250"
# num2 = int(text)
# print(num2, type(num2))   # 250 <class 'int'>


# float → int (decimal part is removed, not rounded)
# pi = 3.14159
# num = int(pi)
# print(num, type(num))   # 3 <class 'int'>

# # int → float
# age = 21
# age_float = float(age)
# print(age_float, type(age_float))   # 21.0 <class 'float'>



# print(round(3.14159))      # 3
# print(round(3.7))          # 4
# print(round(3.14159, 2))   # 3.14 (2 decimal places)
# print(round(5.678, 1))     # 5.7



# remove negative sign
 
# print(abs(-10))    # 10
# print(abs(7))      # 7
# print(abs(-3.5))   # 3.5


# square root

# print(pow(2, 3))      # 8   (2³)
# print(pow(9, 0.5))    # 3.0 (square root)
# print(pow(5, -2))     # 0.04 (1/(5²))



# Find minimum and maximum values

# numbers = [10, 5, 8, 20, 15]

# print(min(numbers))   # 5
# print(max(numbers))   # 20

# print(min(4, 7, 2, 9))   # 2
# print(max(4, 7, 2, 9))   # 9



# import math

# # Square root
# print(math.sqrt(16))   # 4.0

# # Factorial
# print(math.factorial(5))   # 120

# # Floor and ceil
# print(math.floor(3.7))   # 3
# print(math.ceil(3.2))    # 4

# # Trigonometry
# print(math.sin(math.pi/2))   # 1.0
# print(math.cos(0))           # 1.0
