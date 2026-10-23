from pydantic import BaseModel, field_validator

class Student(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def check_name(cls, value):
        if len(value) < 3:
            raise ValueError("Name is too short")
        return value

s1 = Student(name="Aman")
print(s1.name)