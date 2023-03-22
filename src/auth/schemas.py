from pydantic import BaseModel
from src.core.schemas import Token

class LoginRequestSchema(BaseModel):
  email: str
  password: str

class LoginResponseSchema(Token):
  pass

class SignUpRequestSchema(LoginRequestSchema):
  name: str
