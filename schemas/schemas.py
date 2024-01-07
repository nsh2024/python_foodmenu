from pydantic import BaseModel


class Users(BaseModel):
    email: str
    password: str


class Menu(BaseModel):
    breakfast: str
    lunch: str
    dinner: str
    lunchbox: str


class Menus(BaseModel):
    date: str
    menu: Menu
