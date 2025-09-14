
# (a) Add element

s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}



# (b) Multiple elements add

s.update([5, 6, 7])
print(s)  # {1, 2, 3, 4, 5, 6, 7}



# (c) Remove element

s.remove(3)     # Agar element nahi hoga to error aayega
s.discard(10)   # Agar element nahi hai to error nahi aayega
print(s)



# (d) Pop (random element hata deta hai)

removed = s.pop()
print("Removed:", removed)
print("Updated set:", s)



# 🔹 Real-life Example

# 👉 Suppose tumhare pass do students ki hobby sets hain:

student1_hobbies = {"reading", "cricket", "coding"}
student2_hobbies = {"coding", "football", "reading"}

# Common hobbies
print("Common:", student1_hobbies & student2_hobbies)

# All hobbies (without duplicates)
print("All:", student1_hobbies | student2_hobbies)

# Unique hobbies of student1
print("Unique to Student1:", student1_hobbies - student2_hobbies)
