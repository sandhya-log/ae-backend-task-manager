from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.models import Task, User
from app.schemas.task import TaskCreate,TaskResponse
from app.dependencies.auth import get_current_user


router = APIRouter(
    prefix= "/tasks",
    tags= ["Tasks"]
)

@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)

def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_task = Task(
        title = task.title,
        description= task.description,
        user_id = current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task