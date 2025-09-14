# 1. Local Variable
# Jo variable function ke andar define hota hai, uska scope sirf us function ke andar hota hai.

def my_function():
    x = 10   # local variable
    print("Inside function:", x)

my_function()
# print(x)  # ❌ Error, kyunki x function ke bahar exist nahi karta
# 👉 Yaha x sirf function ke andar accessible hai. Function ke bahar print karne par error aayega.


# 2. Global Variable
# Jo variable function ke bahar define hota hai, vo program ke har jagah accessible hota hai.

y = 50  # global variable

def show():
    print("Inside function:", y)

show()
print("Outside function:", y)
# 👉 Yaha y har jagah accessible hai.




# 3. Local variable same name as global
# Agar function ke andar global ke naam ka hi variable banado to vo local maana jaata hai.

z = 100

def test():
    z = 20   # ye local hai
    print("Inside function:", z)

test()
print("Outside function:", z)



# 4. global keyword use karke function ke andar global variable ko modify karna

# By default function ke andar same naam ka variable banane se vo local hota hai.
# Agar hume global variable ko modify karna ho to global keyword use karna padta hai.

a = 5

def change():
    global a
    a = 50   # ab global variable update hoga
    print("Inside function:", a)

change()
print("Outside function:", a)


# 5. nonlocal keyword (nested functions ke liye)
# Agar function ke andar ek nested function hai aur hume parent function ke variable ko modify karna ho to nonlocal use karte hain.

def outer():
    b = 10

    def inner():
        nonlocal b
        b = 20
        print("Inside inner:", b)

    inner()
    print("Inside outer:", b)

outer()