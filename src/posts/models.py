from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.core.models import ModelBase

class Post(ModelBase):
  __tablename__ = "posts"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(256), nullable=False)
  content = Column(String(256))
  owner_id = Column(Integer, ForeignKey("users.id"), index=True)

  owner = relationship("User", back_populates="posts")
