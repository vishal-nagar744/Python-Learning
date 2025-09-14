# What is a Function?

# A function is a block of code that performs a specific task.
# Instead of writing the same code again and again, we put it inside a function and call it whenever needed.

# 🔹 Defining a Function

# We use the def keyword to define a function.


# Function Definition
def greet():
    print("Hello, welcome to Python functions!")


# Here:
# def → keyword to define a function.
# greet → function name.
# () → parentheses (can take inputs later).
# : → start of function block.
# Inside block → the code that runs when function is called.


# 🔹 Calling a Function
# To run the function, just use its name followed by parentheses:

# Function Call
greet()



# 🔹 Functions with Parameters
# We can pass data (inputs) to functions.

def greet_user(name):
    print("Hello", name, "Welcome to Python!")

# Calling with argument
greet_user("Vishal")



# 🔹 Functions with Return Values
# Sometimes we want the function to give back a result.

def add(a, b):
    return a + b

# Calling and storing result
result = add(5, 7)
print("The sum is:", result)
