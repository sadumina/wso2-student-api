from fastapi import FastAPI

app = FastAPI(title="Student API", version="1.0")

students = [
    {"id": 1, "name": "Ayesha", "course": "IT", "year": 3},
    {"id": 2, "name": "Nimal", "course": "CS", "year": 2},
    {"id": 3, "name": "Kavindu", "course": "SE", "year": 4},
]

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = next((s for s in students if s["id"] == student_id), None)
    return student or {"error": "Not found"}

