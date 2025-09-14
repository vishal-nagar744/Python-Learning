# 🔹 1. for loop with Iterables
# 👉 An iterable means anything you can loop over (list, string, tuple, dictionary, set).


# Loop over a list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Loop over a string:
for ch in "Hello":
    print(ch)


# Loop over a dictionary:
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)




# 🔹 while Loop
# 👉 A while loop keeps running as long as a condition is True.
# When the condition becomes False, the loop stops.
# 🖥 Syntax:   

# while condition:
    # code to execute repeatedly


# 🔹 Example 1: Simple Counter
i = 1
while i <= 5:   # loop runs until i is greater than 5
    print("Number:", i)
    i += 1      # increment i




# 🔹 Example 3: while with break
i = 1
while i <= 10:
    if i == 5:
        print("Breaking loop at i =", i)
        break
    print(i)
    i += 1



# 🔹 Example 4: while with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue   # skip when i=3
    print(i)





# 🔹 Common Use Cases of while Loop:
# When number of iterations is unknown (until condition is met).
# Waiting for user input until they enter correct data.

password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access Granted ✅")

# Games → run loop until game over.
# Reading data streams → process until no more data.