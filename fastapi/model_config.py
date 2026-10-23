from pydantic import BaseModel, ConfigDict

class Student(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    name: str

s1 = Student(name="  Aman  ")

print(s1.name)