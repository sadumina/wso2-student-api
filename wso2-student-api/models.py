from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    year: int
    enrollments: List["Enrollment"] = Relationship(back_populates="student")

class Course(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    code: str
    credits: int
    enrollments: List["Enrollment"] = Relationship(back_populates="course")

class Enrollment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(foreign_key="student.id")
    course_id: int = Field(foreign_key="course.id")
    student: Optional[Student] = Relationship(back_populates="enrollments")
    course: Optional[Course] = Relationship(back_populates="enrollments")
