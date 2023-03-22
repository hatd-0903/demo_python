import enum
from sqlalchemy import Enum, Column, Integer, String
from sqlalchemy.orm import relationship

from src.core.models import ModelBase

from src.posts.models import Post

# https://fastapi.tiangolo.com/tutorial/sql-databases/
class UserRole(enum.Enum):
    admin = 1
    user = 2

class User(ModelBase):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(256), nullable=False)
  email = Column(String(256), nullable=False, unique=True, index=True)
  hashed_password = Column(String(256))
  role = Column(Enum(UserRole))

  posts = relationship(Post, back_populates="owner")
