# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Student(BaseModel):
#     name: str
#     age: int

# @app.get("/student", response_model=Student)    #Tells FastAPI to return data according to the Student model.
# def get_student():
#     return {"name": "Aman", "age": 20}

#------------------------------------------------

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int

@app.get("/student", response_model=Student)  #Tells FastAPI to return data according to the Student model.
def get_student():
    return {
        "name": "Aman",
        "age": 20,
        "password": "12345"
    }