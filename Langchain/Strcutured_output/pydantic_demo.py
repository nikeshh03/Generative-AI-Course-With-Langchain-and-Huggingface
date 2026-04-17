from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    
    name : str = 'guest' #default value if the value not given
    age : Optional[int] = None
    email : EmailStr #built in validation for email strcture validation
    cgpa : float = Field(gt=0, lt=10, default=4, description="A decimal value which defines CGPA of a student")

new_student = {'name': 'nikesh', 'age':'24', 'email' : 'abc@gmail.com'} #pydantic handle the type conversion in the background if the data is integer but datatype is not int

student = Student(**new_student)
student_json = student.model_dump_json()
print(student_json)

# print(student)