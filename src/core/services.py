from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.dependencies import get_db

class BaseServices:

  def __init__(self, db: Session = Depends(get_db)):
    self.db = db
