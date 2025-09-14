# conditions_demo.py
# -------------------------------------------
# Python Conditional Statements - Quick Demo
# -------------------------------------------

# 1. Simple if
x = 10
if x > 5:
    print("1. x is greater than 5")

# 2. if-else
age = 18
if age >= 18:
    print("2. You are an adult")
else:
    print("2. You are a minor")

# 3. if-elif-else
marks = 72
if marks >= 90:
    print("3. Grade: A")
elif marks >= 75:
    print("3. Grade: B")
elif marks >= 50:
    print("3. Grade: C")
else:
    print("3. Grade: Fail")

# 4. Nested conditions
num = -5
if num >= 0:
    if num == 0:
        print("4. Number is zero")
    else:
        print("4. Number is positive")
else:
    print("4. Number is negative")

# 5. Using logical operators (and, or, not)
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("5. Login successful")
else:
    print("5. Invalid credentials")

# Example with OR
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("5. Weekend")
else:
    print("5. Weekday")

# Example with NOT
is_logged_in = False
if not is_logged_in:
    print("5. Please log in first")

# 6. Short-hand if (Ternary Operator)
a = 10
b = 20
print("6. a is greater") if a > b else print("6. b is greater")

# 7. Membership operators in condition
fruits = ["apple", "banana", "mango"]
if "apple" in fruits:
    print("7. Apple is in the list")

if "cherry" not in fruits:
    print("7. Cherry is not in the list")

# 8. Mini Login System (Practice)
print("\n--- Mini Login System ---")
saved_username = "admin"
saved_password = "pass123"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username == saved_username:
    if input_password == saved_password:
        print("Login Successful ✅")
    else:
        print("Wrong Password ❌")
else:
    print("User not found ❌")
