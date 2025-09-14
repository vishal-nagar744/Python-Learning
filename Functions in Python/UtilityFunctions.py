

# 1. Factorial Function
def factorial(n):
    """Function to calculate factorial of a number"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 2. Fibonacci Function
def fibonacci(n):
    """Function to generate Fibonacci series up to n terms"""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


# 3. Prime Number Check
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 4. GCD (Greatest Common Divisor) - using Euclidean Algorithm
def gcd(a, b):
    """Return GCD of two numbers"""
    while b:
        a, b = b, a % b
    return a


# 5. Reverse String
def reverse_string(s):
    """Return reversed string"""
    return s[::-1]


# -------------------------
# Function Calling Examples
# -------------------------
if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("First 10 Fibonacci numbers:", fibonacci(10))
    print("Is 29 prime?:", is_prime(29))
    print("GCD of 48 and 18:", gcd(48, 18))
    print("Reverse of 'Python':", reverse_string("Python"))
