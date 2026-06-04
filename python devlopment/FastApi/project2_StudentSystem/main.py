from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    subject: str

students: List[Student] = []


@app.get("/")
def read_root():
    return {"message": "Welcome to student registration portal"}


@app.get("/students")
def get_students():
    return students


@app.post("/add_students")
def add_student(student: Student):
    students.append(student)
    return student


@app.put("/Update_students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error": "Student not found"}

@app.delete("/Delete_students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(index)
            return deleted_student

    return {"error": "Student  not found"}