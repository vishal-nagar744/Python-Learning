# File handling ka matlab hota hai data ko file me read/write/store karna.
# Sabse common modes:

# "r" → read
# "w" → write (purani file overwrite kar dega)
# "a" → append (purani file me add karega)
# "r+" / "w+" → read + write
# Example:

# Writing into a file
with open("data.txt", "w") as f:
    f.write("Hello, Student Management System\n")

# Appending into a file
with open("data.txt", "a") as f:
    f.write("This line is appended!\n")

# Reading file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)


# 🔹 2. Read & Write Example
# Writing to a file

f = open("demo.txt", "w")
f.write("Hello, this is my first file handling program.\n")
f.write("Python is amazing!\n")
f.close()


# Reading from a file

f = open("demo.txt", "r")
content = f.read()   # pura file read karega
print(content)
f.close()



# 🔹 3. Read Methods

f = open("demo.txt", "r")
print(f.read())      # pura file
print(f.read(10))    # pehle 10 characters
print(f.readline())  # ek line
print(f.readlines()) # list of lines
f.close()


# 🔹 5. With Statement (Best Practice ✅)
# Tumhe close() likhne ki zarurat nahi hoti.

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)



# 🔹 6. File Pointer
# f.tell() → current position
# f.seek(n) → cursor ko n position par le jaata hai

with open("demo.txt", "r") as f:
    print(f.read(5))
    print(f.tell())   # cursor position
    f.seek(0)         # cursor reset
    print(f.read(5))


# 🔹 7. Working with Files (Practical Example)
# Write student data

with open("students.txt", "w") as f:
    f.write("Name, Roll, Marks\n")
    f.write("Honey, 1, 95\n")
    f.write("Vishal, 2, 88\n")


#  Read student data

with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())   



#  🔹 8. Delete or Rename File

import os

# delete file
os.remove("demo.txt")

# rename file
os.rename("students.txt", "my_students.txt")     