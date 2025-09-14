# basics.py
# Ye script variables aur data types dikhata hai

# Integer variable
age = 21
print("Age:", age, "Type:", type(age))

# Float variable
pi = 3.14159
print("Pi value:", pi, "Type:", type(pi))

# String variable
name = "Vishal"
print("Name:", name, "Type:", type(name))

# Boolean variable
is_student = True
print("Is Student?", is_student, "Type:", type(is_student))

# Multiple variables ek line me
x, y, z = 10, 20.5, "Python"
print("x:", x, "Type:", type(x))
print("y:", y, "Type:", type(y))
print("z:", z, "Type:", type(z))

# Constant (by convention uppercase, but Python me real constant nahi hote)
PI = 3.14
print("Constant PI:", PI)

# Type conversion examples
num_str = "100"
num_int = int(num_str)   # string → int
print("Converted:", num_int, "Type:", type(num_int))

float_num = float(num_int)  # int → float
print("Converted:", float_num, "Type:", type(float_num))
