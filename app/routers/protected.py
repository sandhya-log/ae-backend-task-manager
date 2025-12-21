from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.database.models import User

router = APIRouter(
    prefix="/protected",
    tags=["Protected"]
)

@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return{
        "id" : current_user.id,
        "email" : current_user.email
    }