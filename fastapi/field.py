from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str
    age: int = Field(gt=0, lt=100)

s1 = Student(name="Aman", age=20)

print(s1)