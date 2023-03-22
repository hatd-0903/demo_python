import requests
from fastapi import APIRouter

from src.external.schemas import User

router = APIRouter(prefix="/external")

@router.get("/users")
def get_users():
  r = requests.get("https://reqres.in/api/users")
  return r.text


@router.post("/users")
def creat_users(form_data: User):
  r = requests.post("https://reqres.in/api/users", data=form_data.dict())
  return r.text

@router.put("/users/{user_id}")
def creat_users(
  user_id: int,
  form_data: User
):
  url = f"https://reqres.in/api/users/{user_id}"
  r = requests.put(url, data=form_data.dict())
  return r.text

@router.delete("/users/{user_id}")
def creat_users(
  user_id: int
):
  url = f"https://reqres.in/api/users/{user_id}"
  r = requests.delete(url)
  return r.text
