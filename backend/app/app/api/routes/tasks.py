from typing import List
from fastapi import APIRouter, Depends
from fastapi.concurrency import run_in_threadpool

from app.api.dependencies.authentication import oauth2_scheme, get_current_user
from app.models.pydantic.task import Task
from app.models.pydantic.user import User
from app.models.tortoise.task import Task_DB
from app.worker import add_periodic

router = APIRouter()

@router.get('/all', response_model=List[Task])
async def list_tasks(current_user: User = Depends(get_current_user)):
    tasks = await Task_DB.filter(user=current_user).all()
    return tasks

@router.post('/add')
async def add_task(task: Task = None, current_user: User = Depends(get_current_user)):
    await Task_DB.create(**task.dict())
    await run_in_threadpool(add_periodic({"hour": 7, "minute": 0, "day": 1}, **Task.dict()))
    return {"success": True}
