# 🔑 Python Dictionary – Basics
# 👉 Dictionary ek key-value pair collection hai. Matlab data ko aise store karte hain:

dictionary = {
    "name": "Vishal",
    "age": 21,
    "city": "Indore"
}


# Keys (unique hote hain) → "name", "age", "city"
# Values → "Vishal", 21, "Indore"

# 🛠 Dictionary Operations

# Accessing Values
student  = { "name": "John", "age": 22, "city": "New York" }
print(student["name"])  # Output: John
print(student["age"])   # Output: 22
print(student["city"])  # Output: New York

# Adding Entries
student["college"] = "IIT Bombay"
print(student)  # Output: {'name': 'John', 'age': 22, 'city': 'New York', 'college': 'IIT Bombay'}

# Updating Entries
student["age"] = 20
print(student)  # {'name': 'John', 'age': 20, 'city': 'New York', 'college': 'IIT Bombay'}

# Deleting Entries

# Delete using del
del student["city"]
print(student)  # {'name': 'John', 'age': 20, 'college': 'IIT Bombay'}

# Specific key delete
student.pop("name")
print(student)  

# Last inserted key-value delete
student.popitem()
print(student)  

# Clear full dictionary
student.clear()
print(student)  # {}


# Dictionary Keys, Values, Items

person = {"name": "Honey", "age": 21, "country": "India"}

print(person.keys())    # dict_keys(['name', 'age', 'country'])
print(person.values())  # dict_values(['Honey', 21, 'India'])
print(person.items())   # dict_items([('name', 'Honey'), ('age', 21), ('country', 'India')])



# Looping in Dictionary

for key in person:
     print(key, "->", person[key])


# .items() ke saath:
for key, value in person.items():
    print(key, ":", value)


# Nested Dictionary (Dictionary inside Dictionary)

Students = { 
      "101": { "name": "Alice", "age": 20, "city": "New York" },
      "102": { "name": "Bob", "age": 22, "city": "Los Angeles" },
      "103": { "name": "Charlie", "age": 21, "city": "Chicago" }
}
print( Students["101"]["name"] )# Output: Alice