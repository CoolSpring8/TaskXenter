from fastapi import APIRouter

from app.api.routes import user, tasks

router = APIRouter()
router.include_router(user.router, tags=["user"], prefix="/user")
router.include_router(tasks.router, tags=["tasks"], prefix="/tasks")
