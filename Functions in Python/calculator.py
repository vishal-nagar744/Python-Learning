# Q2. Calculator using Functions

# 👉 Ek function calculator(a, b, operator) banao jo +, -, *, / operations kare.
# User se 2 numbers aur ek operator input lo.
# Function ko call karke result print karo.
# Agar invalid operator ho to "Invalid Operator" return kare.

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b if b != 0 else "Division by zero error"
    else:
        return "Invalid Operator"

# User input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

# Function call
result = calculator(num1, num2, op)
print("Result:", result)
