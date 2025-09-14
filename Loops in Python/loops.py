# 🔹 1. for loop with range()

# 👉 range() is used to generate numbers in a sequence.
# Syntax:

# range(start, stop, step)

# start → from where to begin (default = 0)
# stop → till where to go (exclusive)
# step → increment/decrement (default = 1)

# exmaple:- 

for i in range(5): 
    print(i)  # Output: 0, 1, 2, 3, 4

# Print 1 to 5
for i in range(1, 6):
    print(i)    


# Print even numbers
for i in range(0, 11, 2):
    print(i)