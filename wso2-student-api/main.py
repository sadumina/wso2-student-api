from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from models import Student, Course, Enrollment
from database import init_db, get_session
from typing import List

app = FastAPI(title="Academy API", version="2.0.0")
init_db()

# Dependency
def get_db():
    with get_session() as session:
        yield session

@app.get("/students", response_model=List[Student])
def get_students(db: Session = Depends(get_db)):
    return db.exec(select(Student)).all()

@app.post("/students", response_model=Student)
def add_student(student: Student, db: Session = Depends(get_db)):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student
