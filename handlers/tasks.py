from database import get_db_connecttion
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
    result: list[Task] = []
    cursor = get_db_connecttion().cursor()
    tasks = cursor.execute("SELECT * FROM Tasks").fetchall()
    for task in tasks:
        result.append(Task(
            id=task[0],
            name=task[1],
            pomodoro_count=task[2],
            category_id=task[3]
        ))
    return result


# @router.get("/")
# async def create_task(body: Task):
#     return {"text": body}


@router.post(
    "/",
    response_model=Task
)
async def create_task(task: Task):
    connection = get_db_connecttion()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Tasks (name, pomodoro_count, category_id) VALUES (?, ?, ?)",
                   (task.name, task.pomodoro_count, task.category_id))
    connection.commit()
    connection.close()
    fixtures_tasks.append(task)
    return task


# @router.get("/tasks")
# async def tasks():
#     return {''}


@router.patch(
    "/{task_id}",
    response_model=Task
)
async def update_task(task_id: int, name: str):
    connection = get_db_connecttion()
    cursor = connection.cursor()
    cursor.execute("UPDATE Tasks SET name =? WHERE id =?", (name, task_id))
    connection.commit()
    task = cursor.execute("SELECT * FROM Tasks WHERE id =?", __parameters=(f"{task_id}")).fetchall()[0]
    connection.close()
    return Task(
        id=task[0],
        name=task[1],
        pomodoro_count=task[2],
        category_id=task[3]
    )
    
    # for task in fixtures_tasks:
    #     if task["id"] == task_id:
    #         task["name"] = name
    #         return task
    # raise HTTPException(status_code=404, detail="Task not found")


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