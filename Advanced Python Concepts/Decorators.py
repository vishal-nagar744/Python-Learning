# 🔹 1. Decorator kya hai?

# Decorator ek function hai jo doosre function ke behavior ko modify karta hai without changing its code.
# Iske liye Python me @decorator_name syntax use hota hai.

# 🔹 2. Basic Example (without @)

def greet(func):
    def wrapper():
        print("Hello!")       # extra feature
        func()                # original function
        print("Have a nice day!")
    return wrapper

def say_name():
    print("My name is Honey")

# Decorator lagaya manually
decorated = greet(say_name)
decorated()



# 🔹 3. Same Example (with @)

def greet(func):
    def wrapper():
        print("Hello!")
        func()
        print("Have a nice day!")
    return wrapper

@greet
def say_name():
    print("My name is Honey")

say_name()




# 🔹 4. Decorator with Arguments

def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("❌ Cannot divide by zero!")
            return
        return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    print(f"Result: {a/b}")

divide(10, 2)   # ✅ Result: 5.0
divide(10, 0)   # ❌ Cannot divide by zero!



# 🔹 5. Real-life Examples
# ✅ Logging

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

print(add(5, 3))



# ✅ Authentication (like Flask / FastAPI)

def require_login(func):
    def wrapper(user):
        if not user.get("is_logged_in"):
            print("⚠️ Access Denied!")
            return
        return func(user)
    return wrapper

@require_login
def dashboard(user):
    print(f"Welcome {user['name']}!")

user1 = {"name": "Honey", "is_logged_in": True}
user2 = {"name": "Vishal", "is_logged_in": False}

dashboard(user1)  # ✅ Welcome Honey!
dashboard(user2)  # ⚠️ Access Denied!




# 🔹 6. Decorator with functools.wraps

# Jab hum decorators banate hain, to original function ka naam & docstring overwrite ho jaati hai.
# Isliye functools.wraps use karte hain:

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def hello():
    """This says hello"""
    print("Hello World")

print(hello.__name__)   # hello
print(hello.__doc__)    # This says hello

# 🔹 7. Summary

# Decorator = Function that modifies another function.
# Syntax = @decorator_name
# Uses = Logging, Authentication, Validation, Rate Limiting, API request handling.
# functools.wraps preserve karta hai function metadata.