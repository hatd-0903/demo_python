from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.users.models import User, UserRole

from src.posts.repositories import PostRepositories

def can_edit(post_id: int, db: Session, user: User):
  post = PostRepositories(db).get_post(id=post_id)

  if not post:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="Post not exist"
    )

  if post.owner_id != user.id:
    if user.role != UserRole.admin:
      raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Not permission to this action"
      )

  return True
