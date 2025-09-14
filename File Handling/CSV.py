# A) Write (create) CSV

import csv

students = [
    {"name": "Honey", "roll": 1, "marks": 95.5},
    {"name": "Vishal", "roll": 2, "marks": 88.0},
    {"name": "Aditi", "roll": 3, "marks": 76.5},
]

with open("students.csv", "w", newline = '', encoding="utf-8") as csvfile:
    fieldnames = ["name", "roll", "marks"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # header row
    writer.writerows(students)  # multiple rows
    print("Data written to students.csv")   



# B) Append (add more rows)

new_rows = [
    {"name": "Rohit", "roll": 4, "marks": 82.0},
]

with open("students.csv", "a", newline = '', encoding="utf-8") as csvfile:
    fieldnames = ["name", "roll", "marks"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerows(new_rows)  # multiple rows
    print("Data appended to students.csv")



#  C) Read CSV (strings aate hain → type cast karo)

records = []

with open("students.csv", "r", newline = '', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Type casting
        row['roll'] = int(row['roll'])
        row['marks'] = float(row['marks'])
        records.append(row)

print("Read records:", records)       



# D) Update CSV (simple way = read → modify → overwrite)

# 1) read all
with open("students.csv", "r", newline = '', encoding="utf-8") as csvfile:
        rows = list(csv.DictReader(csvfile))

# 2) modify (e.g., update marks for roll=2)
for row in rows:
     if int(row['roll']) == 2:
          row['marks'] = str(90.0) # DictReader keeps strings; write strings back

# 3) overwrite
with open("students.csv", "w", newline = '', encoding="utf-8") as csvfile:
     fieldnames = rows[0].keys()  # get fieldnames from existing data
     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
     writer.writeheader()  # write header
     writer.writerows(rows)  # write updated rows

print("CSV updated successfully")     