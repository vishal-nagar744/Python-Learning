# 🔹 4. Encapsulation (Data hiding)
# 👉 Hum private variables bana sakte hain (naming: _var ya __var).

class Account:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account(5000)
acc.deposit(2000)
print("💰 Balance:", acc.get_balance())

# print(acc.__balance) ❌ Direct access nahi hoga