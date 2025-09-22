from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int

students = [
    {"id": 1, "name": "Vishal", "age": 21},
    {"id": 2, "name": "Honey", "age": 22}
]

# GET all students
@app.get("/students")
def get_students():
    return students

# GET single student
@app.get("/students/{id}")
def get_student(id: int):
    for s in students:
        if s["id"] == id:
            return s
    return {"error": "Not Found"}

# POST new student
@app.post("/students")
def add_student(student: Student):
    students.append(student.dict())
    return student

# PUT update student
@app.put("/students/{id}")
def update_student(id: int, student: Student):
    for i, s in enumerate(students):
        if s["id"] == id:
            students[i] = student.dict()
            return student
    return {"error": "Not Found"}

# DELETE student
@app.delete("/students/{id}")
def delete_student(id: int):
    global students
    students = [s for s in students if s["id"] != id]
    return {"message": "Deleted!"}
