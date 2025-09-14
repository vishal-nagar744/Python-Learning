# 🔹 What are Nested Loops?
# A loop inside another loop.
# 👉 Outer loop runs first, and for each iteration of the outer loop, the inner loop runs completely.


# 🔹 Example 1: Simple Nested Loop
for i in range(3):        # Outer loop
    for j in range(2):    # Inner loop
        print(f"i={i}, j={j}")



# Example 2: Multiplication Table
for i in range(1, 4):      # Rows
    for j in range(1, 4):  # Columns
        print(i * j, end=" ")
    print()



# 🔹 Example 3: Pattern Printing
for i in range(5):        # Rows
    for j in range(i + 1):  # Columns
        print("*", end=" ")
    print()



# 🔹 Example 4: Nested While Loops
i = 1
while i <= 3:       # Outer loop
    j = 1
    while j <= 2:   # Inner loop
        print(f"(i={i}, j={j})")
        j += 1
    i += 1