# 🔹 5. Polymorphism (Same method, different behavior)
# 👉 Ek hi method alag-alag objects pe alag tarah se behave kare.

class Dog:
    def sound(self):
        print("🐶 Bark")

class Cat:
    def sound(self):
        print("🐱 Meow")

# Polymorphism in action
for animal in [Dog(), Cat()]:
    animal.sound()





# ✅ Summary

# Class & Object → Blueprint & instance

# Constructor → Object banate hi run hota hai

# Inheritance → Code reuse (Parent → Child)

# Encapsulation → Data hiding (__var)

# Polymorphism → Same function, different behavior