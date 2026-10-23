from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi_new.FastAPI_Task.dependencies import get_message

router = APIRouter()
tasks = []

class Task(BaseModel):
    id: int
    title: str

# CREATE
@router.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {"message": "Task added"}

# READ
@router.get("/tasks")
def get_tasks(message: str = Depends(get_message)):
    return {"message": message, "tasks": tasks}

# UPDATE
@router.put("/tasks/{task_id}")
def update_task(task_id: int, new_task: Task):
    for task in tasks:
        if task.id == task_id:
            task.title = new_task.title
            return {"message": "Task updated"}
    raise HTTPException(status_code=404, detail="Task not found")

# DELETE
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")