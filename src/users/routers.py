from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.dependencies import get_db

from src.auth.services import get_current_user

from src.users.schemas import User

router = APIRouter(prefix="/users")

@router.get("/me", response_model=User)
def read_users_me(
  current_user: User = Depends(get_current_user)
) -> User:
  return current_user
