from src.core.repositories import BaseRepositories

from src.posts.models import Post
from src.posts.schemas import PostCreate, PostEdit

from src.users.models import User

class PostRepositories(BaseRepositories):
  def get_posts(self, skip: int = 0, limit: int = 100):
    return self.db.query(Post).offset(skip).limit(limit).all()

  def get_post(self, id: int):
    return self.db.query(Post).filter(Post.id==id).first()

  def create_post(self, post: PostCreate, user: User):
    db_post = Post(
      title=post.title,
      content=post.content,
      owner_id=user.id
    )
    self.db.add(db_post)
    self.db.commit()
    self.db.refresh(db_post)
    return db_post

  def edit_post(self, post: PostEdit, id: int):
    query = self.db.query(Post).filter(Post.id==id)
    db_post = query.first()

    update_data = post.dict(exclude_unset=True)
    query.update(update_data, synchronize_session=False)

    self.db.commit()
    self.db.refresh(db_post)
    return db_post

  def delete_post(self, id: int):
    self.db.query(Post).filter(Post.id==id).delete()
    self.db.commit()

    return True
