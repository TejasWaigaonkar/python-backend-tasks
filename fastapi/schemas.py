from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None

class StudentRead(BaseModel):
    id: int
    name: str
    age: int

s1 = StudentCreate(name="Aman", age=20)
print(s1)