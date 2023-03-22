from passlib.context import CryptContext
from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.dependencies import get_db
from src.core.repositories import BaseRepositories

from src.auth.schemas import SignUpRequestSchema

from src.users.models import User, UserRole

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRepositories(BaseRepositories):
  def get_user_by_email(self, email: str):
    return self.db.query(User).filter(User.email == email).first()

  def create_user(self, user: SignUpRequestSchema):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        email=user.email,
        name=user.name,
        role=UserRole.user,
        hashed_password=hashed_password
    )
    self.db.add(db_user)
    self.db.commit()
    self.db.refresh(db_user)
    return db_user
