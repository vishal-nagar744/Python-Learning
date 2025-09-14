import sqlite3

# Connect to database (file create ho jayega agar nahi hai)
conn = sqlite3.connect("students.db")

# Create cursor (for executing SQL queries)
cursor = conn.cursor() 


# create table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER
)
""")

print("✅ Table created successfully!")

conn.commit()
conn.close()




# insert data into table
import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Insert data 
cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Rahul",85))
cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Mohit",90))

print("✅ Data inserted successfully!")

conn.commit()
conn.close()


# Read data from table
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("📂 All Students:")
for row in rows:
    print(row)

conn.close()



# Update & Delete data in table
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Update
cursor.execute("UPDATE students SET marks = 95 WHERE name = 'Rahul'")

# Delete
cursor.execute("DELETE FROM students WHERE name = 'Sneha'")

conn.commit()
conn.close()
print("✅ Update & Delete done!")
