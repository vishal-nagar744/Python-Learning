# 🔹 2. Constructor (init)

# 👉 Constructor ek special method hai jo object create hote hi call hota hai.
# __init__ me attributes (variables) set karte hain.

class Student:
    def __init__(self, name, age):   # constructor
        self.name = name
        self.age = age
    
    def show_info(self):
        print(f"👨‍🎓 Name: {self.name}, Age: {self.age}")

# Object with constructor
s1 = Student("Vishal", 21)
s2 = Student("Honey", 22)

s1.show_info()
s2.show_info()