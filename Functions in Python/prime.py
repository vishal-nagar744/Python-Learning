# Q1. Prime Number Checker (with functions)
# 👉 Ek function banao jo input number lega aur check karega ki wo prime hai ya nahi.
# Function ka naam: is_prime(number)
# Return karega True ya False.
# Main program me user se input lo aur function call karke result print karo.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Main program
user_input = int(input("Enter a number: "))
if is_prime(user_input):
    print(user_input, "is a prime number.")
else:
    print(user_input, "is not a prime number.")
