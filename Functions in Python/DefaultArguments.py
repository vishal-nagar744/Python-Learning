# 🔹 Default Arguments

# Default argument ka matlab hota hai ki agar function call karte time koi value pass na karein, to ek default value use ho jaye.
# Example 1: Greeting Function

def greet(name="Guest"):
    print(f"Hello, {name}!")

# Call with argument
greet("Vishal")

# Call without argument
greet()


# 🔹 Keyword Arguments

# Keyword arguments me hum directly parameter ka naam likh ke value dete hain.
# Isse order important nahi hota.

# Example 2: Student Info


def student_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Normal (positional arguments)
student_info("Rohit", 21, "Delhi")

# Keyword arguments (order badal sakte hain)
student_info(age=22, city="Indore", name="Vishal")
