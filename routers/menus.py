from fastapi import APIRouter

router = APIRouter()


@router.get("/menus", tags=["menus"])
def get_menus():
    return {"menus": "menu1"}
