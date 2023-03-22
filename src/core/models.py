from sqlalchemy import func, Column, DateTime

from db.database import Base


class ModelBase(Base):

    __abstract__ = True

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
