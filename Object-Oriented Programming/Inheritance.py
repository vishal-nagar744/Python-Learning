# 🔹 3. Inheritance (Reuse code)
# 👉 Ek class dusri class ki properties aur methods use kar sakti hai.

# Parent class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

# Child class
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)   # parent constructor call
        self.roll = roll

    def show(self):
        print(f"👨‍🎓 Name: {self.name}, Roll: {self.roll}")

s = Student("Vishal", 101)
s.greet()   # Parent method
s.show()    # Child method