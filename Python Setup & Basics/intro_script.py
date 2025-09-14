# intro_script.py
# Ye ek basic introduction script hai

# Variables
name = "Vishal"     # string
age = 21            # integer
height = 5.9        # float

# Output using f-string (best way)
print(f"My name is {name}, I am {age} years old, and my height is {height} feet.")

# Output using .format()
print("My name is {}, I am {} years old, and my height is {} feet.".format(name, age, height))

# Output using % formatting
print("My name is %s, I am %d years old, and my height is %.1f feet." % (name, age, height))
