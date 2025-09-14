
import json

students = []      # list to store students records

# Function to add student
def add_student(name, roll, marks):
    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }
    students.append(student)
    print(f"✅ Student {name} added successfully!")    


# Function to display all students
def display_students():
    if not students:
        print("⚠️ No students available.")
    else:
        print("📋 Student Records:")   
        for student in students:
            print(f"Name: {student['name']}, Roll: {student['roll']}, Marks: {student['marks']}") 


# Function to calculate average marks
def calculate_average():
    if not students:
        print("⚠️ No students available to calculate average.")
    else:
        total = 0
        for student in students:
            total += student['marks']
        avg = total / len(students)
        print(f"📊 Average Marks: {avg:.2f}")    


# Search Student by Roll Number 
def search_student(roll):
    for student in students:
        if student['roll'] == roll:
            print(student)       
            return
    print("⚠️ Student not found.")



# Update Student Information
def update_student(roll, new_name=None, new_marks=None):
    for student in students:
        if student['roll'] == roll:
            if new_name: student['name'] = new_name
            if new_marks: student['marks'] = new_marks
            print("Student updated successfully!")
            return
    print("Student not found!")


# delete student 
def delete_student(roll):
    for student in students:
        if student['roll'] == roll:
            students.remove(student)
            print("✅ Student deleted successfully!")
            return
    print("⚠️ Student not found!")


# Highest & Lowest Marks
def highest_marks():
    if not students:
        print("⚠️ No students available to determine highest marks.")
    else:
        highest = max(students, key=lambda x: x['marks'])
        print(f"🏆 Highest Marks: {highest['marks']} (Student: {highest['name']})")

def lowest_marks():
    if not students:
        print("⚠️ No students available to determine lowest marks.")
    else:
        lowest = min(students, key=lambda x: x['marks'])
        print(f"📉 Lowest Marks: {lowest['marks']} (Student: {lowest['name']})")


#  Save Data to File
#  file (students.json)

def save_data():
    with open("students.json", "w") as file:
       json.dump(students, file)
    print("✅ Data saved successfully!")

def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    print("✅ Data loaded successfully!")


# Menu-driven program
def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Calculate Average Marks")
        print("4. Search Student by Roll Number")
        print("5. Update Student Information")
        print("6. Delete Student")
        print("7. Show Highest & Lowest Marks")
        print("8. Save Data")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            name = input("Enter student name: ")
            roll = input("Enter student roll number: ")
            marks = float(input("Enter student marks: "))
            add_student(name, roll, marks)

        elif choice == '2':
            display_students()

        elif choice == '3':
            calculate_average()

        elif choice == '4':
            roll = input("Enter student roll number to search: ")
            search_student(roll) 

        elif choice == '5':
            roll = input("Enter student roll number to update: ")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_marks = input("Enter new marks (leave blank to keep current): ")
            update_student(roll, new_name if new_name else None, float(new_marks) if new_marks else None)

        elif choice == "6":
            roll = input("Enter student roll number to delete: ")
            delete_student(roll)


        elif choice == "7":
            highest_marks()
            lowest_marks()

        elif choice == "8":
            save_data()

        elif choice == "9":
            print("👋 Exiting Student Management System. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")



if __name__ == "__main__":
    main()