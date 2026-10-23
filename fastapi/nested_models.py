from pydantic import BaseModel

class Address(BaseModel):
    city: str

class Student(BaseModel):
    name: str
    address: Address

s1 = Student(
    name="Aman",
    address=Address(city="Pune")
)

print(s1.name)
print(s1.address.city)