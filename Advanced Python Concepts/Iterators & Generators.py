# 🔹 1. Iterator kya hai?

# Iterator ek aisa object hai jo ek-ek karke values return karta hai.
# Har iterator ke paas do methods hote hain:

# __iter__()
# __next__()

# Example:

nums = [1, 2, 3]
it = iter(nums)   # iterator banaya

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # ❌ StopIteration error


# 👉 Jab values khatam ho jaati hain, StopIteration error aata hai.



# 🔹 2. Custom Iterator

# Hum apna khud ka iterator bana sakte hain class banake.
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):   # iterator return
        return self
    
    def __next__(self):   # next value return
        if self.current <= self.end:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration
        
for num in Counter(1, 5):
    print(num)     


# 🔹 3. Generator

# Generator ek special function hai jo yield keyword use karta hai.
# yield ek-ek value return karta hai without stopping function.

def my_generator():
    yield 1
    yield 2
    yield 3

for val in my_generator():
    print(val)



# 🔹 4. Example: Fibonacci with Generator    

def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)



# ✅ Summary:

# Iterator → Object with __iter__() & __next__()

# Generator → Function with yield, easy iterators

# Best use → Large data, streaming, pipelines