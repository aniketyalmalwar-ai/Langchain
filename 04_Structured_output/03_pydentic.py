from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, le=10, description="A decimal value representing cgpa of a student")

new_student = {
    'name': "Aniket",
    'age': 25,
    'email': "aniket@gmail.com",
    'cgpa': 8.5
}

new_student2 = {
    'name': "Aniket",
    'age': '25',
    'email': "aniket@gmail.com",
    'cgpa': 9.2
}  # Type conversion from str to int if possible; if not, throws error.

student = Student(**new_student)
print(student)

student2 = Student(**new_student2)
print(student2)

student_dic = dict(student)
student_json = student.model_dump_json()

print(student_dic)
print(student_json)