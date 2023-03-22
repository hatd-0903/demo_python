import enum
from pydantic import BaseModel

class Post(BaseModel):
  id: str
  title: str
  content: str | None

  class Config:
    orm_mode = True

class PostCreate(BaseModel):
  title: str
  content: str | None

class PostEdit(BaseModel):
  title: str | None
  content: str | None
