from fastapi import APIRouter
from dao import user_handler
from schemas.schemas import Users

router = APIRouter()


@router.get("/users", tags=["users"])
def get_users():
    return user_handler.read_user_data()


@router.post("/users", tags=["users"])
def get_users(user: Users):
    print(user.email)
    print(user.password)
    user_handler.write_menu_data(user)
