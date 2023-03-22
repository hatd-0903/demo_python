from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.dependencies import get_db

from src.auth.services import get_current_user

from src.users.schemas import User

from src.posts.schemas import Post, PostCreate, PostEdit
from src.posts.repositories import PostRepositories
from src.posts.services import can_edit


router = APIRouter(prefix="/posts")

@router.get("/", response_model=list[Post])
def get_posts(
  skip: int = 0, limit: int = 10,
  current_user: User = Depends(get_current_user),
  db: Session = Depends(get_db)
) -> list[Post]:
  return PostRepositories(db).get_posts(skip=skip, limit=limit)

@router.get("/{post_id}", response_model=Post)
def get_post(
  post_id: int,
  current_user: User = Depends(get_current_user),
  db: Session = Depends(get_db)
) -> Post:
  post = PostRepositories(db).get_post(id=post_id)
  if not post:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="Post not exist"
    )
  return post

@router.post("/", response_model=Post)
def create(
  form_data: PostCreate,
  current_user: User = Depends(get_current_user),
  db: Session = Depends(get_db)
) -> Post:
  return PostRepositories(db).create_post(form_data, current_user)

@router.put("/{post_id}", response_model=Post)
def edit(
  post_id: int,
  form_data: PostEdit,
  current_user: User = Depends(get_current_user),
  db: Session = Depends(get_db)
) -> Post:
  can_edit(post_id, db=db, user=current_user)

  return PostRepositories(db).edit_post(form_data, id=post_id)


@router.delete("/{post_id}", response_model=str)
def delete(
  post_id: int,
  current_user: User = Depends(get_current_user),
  db: Session = Depends(get_db)
) -> str:
  can_edit(post_id, db=db, user=current_user)

  PostRepositories(db).delete_post(id=post_id)

  return "success"
