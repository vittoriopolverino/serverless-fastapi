from typing import Union

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class User(BaseModel):
    first_name: str
    last_name: str
    is_registered: Union[bool, None] = None


@router.get("/")
async def get_users():
    return {"message": "Users!"}


@router.put("/{user_id}")
def update_user(user_id: int, user: User):
    return {"user_firstname": user.first_name, "user_id": user_id}
