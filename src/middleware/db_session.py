from fastapi import Request, Response
from db.database import SessionLocal
from starlette.middleware.base import BaseHTTPMiddleware

class DbSessionMiddleware(BaseHTTPMiddleware):
  async def dispatch(self, request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
