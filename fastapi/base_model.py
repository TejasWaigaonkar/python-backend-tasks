from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int

s1 = Student(name="Aman", age=20)

print(s1.name)
print(s1.age)