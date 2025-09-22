from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy Data
students = [
    {"id": 1, "name": "Vishal", "age": 21},
    {"id": 2, "name": "Honey", "age": 22}
]

# 1. GET all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

# 2. GET student by id
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    student = next((s for s in students if s["id"] == id), None)
    return jsonify(student) if student else ("Not Found", 404)

# 3. POST new student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    new_id = max(s["id"] for s in students) + 1
    new_student = {"id": new_id, "name": data["name"], "age": data["age"]}
    students.append(new_student)
    return jsonify(new_student), 201

# 4. PUT (Update student)
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.json
    for student in students:
        if student["id"] == id:
            student.update(data)
            return jsonify(student)
    return ("Not Found", 404)

# 5. DELETE student
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return ("Deleted", 204)

if __name__ == "__main__":
    app.run(debug=True)
