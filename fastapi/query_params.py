from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def search(name: str, age: int = 18):
    return {"name": name, "age": age}