from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/all")
async def get_task():
    return {"message": "ok"}


@router.get("/app")
async def create_task():
    return {"text": "app is working"}


@router.post("/task/{task_id}")
async def create_taskid():
    return {"task_id": "id"}


@router.get("/tasks")
async def tasks():
    return {''}