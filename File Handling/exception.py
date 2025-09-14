# 🔹 Syntax of try-except

try:
    # Code jisme error ho sakta hai
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result:", y)

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Invalid input, please enter a number.")




# 🔹 finally block
# finally ka code hamesha run hota hai, chahe exception aaye ya na aaye.
# Mostly resources close karne ke liye use hota hai (jaise file, DB connection).

try:
    f = open("test.txt", "r")
    data = f.read()
    print(data)

except FileNotFoundError:
    print("Error: File not found.")

finally:
    print("Closing file (if opened).")
    try:
        f.close()
    except:
        pass
# 👉 Agar file exist karti hai to data print hoga
# 👉 Agar file nahi hai to error message aayega
# 👉 Lekin finally hamesha chalega.



# ✅ Real-life Example (User Input Division)
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter only numbers.")

else:
    print("Result is:", result)

finally:
    print("Execution completed.")
