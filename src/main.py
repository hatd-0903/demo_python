from fastapi import FastAPI, Request, Response

from db.database import SessionLocal

from src.middleware.db_session import DbSessionMiddleware

from src.auth.routers import router as auth_router
from src.users.routers import router as user_router
from src.posts.routers import router as post_router
from src.external.routers import router as external_router

app = FastAPI()

app.add_middleware(DbSessionMiddleware)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(post_router)
app.include_router(external_router)
