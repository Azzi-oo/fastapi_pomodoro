from fastapi import APIRouter
from pydantic import BaseModel
from fixtures import tasks as fixtures_tasks
from schema.task import *
from fastapi import status, HTTPException


router = APIRouter(prefix="/task", tags=["task"])


@router.get(
    "/all",
    response_model=list[Task],
)
async def get_tasks():
    return fixtures_tasks


@router.get("/")
async def create_task(body: Task):
    return {"text": body}


@router.post(
    "/",
    response_model=Task
)
async def create_task(task: Task):
    fixtures_tasks.append(task)
    return task


@router.get("/tasks")
async def tasks():
    return {''}


@router.patch(
    "/{task_id}",
    response_model=Task
)
async def update_task(task_id: int, name: str):
    for task in fixtures_tasks:
        if task["id"] == task_id:
            task["name"] = name
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_task(task_id: int):
    for index, task in enumerate(fixtures_tasks):
        if task["id"] == task_id:
            del fixtures_tasks[index]
            return {"message": "task deleted"}
        
    return {"message": "task not found"}