# 🔹 1. Context Manager Kya Hai?

# Jab tumhe resource open karna aur properly close karna ho, tab use hota hai.
# Example: file open karna → kaam karna → close karna (warna memory leak/error ho sakta hai).
# Python me with statement isi ke liye use hota hai.

# 🔹 2. Normal Way (without context manager)

f = open("demo.txt", "w")
f.write("Hello Vishal!")
f.close()   # ❌ Agar close() bhool gaye to problem hogi

# 🔹 3. With with Statement (Context Manager)

with open("demo.txt", "w") as f:
    f.write("Hello Honey!")

# ✅ yaha f automatically close ho jayega

# 🔹 4. Custom Context Manager (class se)

class MUContext:
    def __inter__(self):
        print("🔓 Resource Open")
        return "Resource Data"
    
    def __exit__(self, exc_type, exc_value, traceback):     
        print("🔒 Resource Closed")

with MUContext() as resource:
    print("Using:", resource)
    # raise Exception("Some Error")   # Uncomment karke error bhi dekh sakte ho        
    