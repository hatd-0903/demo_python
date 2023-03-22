import enum
from pydantic import BaseModel

class User(BaseModel):
  id: str
  email: str
  name: str
  role: enum.Enum

  class Config:
    orm_mode = True
