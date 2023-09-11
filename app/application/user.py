import uuid

from fastapi import APIRouter

from app.domain.user.repository import UserRepository

router = APIRouter()


@router.get("/users/")
async def read_users():
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.get("/users/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{user_id}")
async def read_user(user_id: uuid.UUID):
    user = UserRepository("").get(user_id=user_id)
    return {"name": user.name, "nickname": user.nickname}
