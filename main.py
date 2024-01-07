from fastapi import FastAPI
from config import settings


app = FastAPI(title=settings.TITLE,
              description=settings.DESCRIPTION,
              version=settings.VERSION,
              contact={
                  "name": settings.NAME,
                  "email": settings.EMAIL
              },
              openapi_tags=settings.TAGS,
              openapi_url=settings.OPENAPI_URL,
              docs_url=settings.DOCUMENTATION_URL
              )


@app.get("/", tags=[])
def index():
    return {"message": "welcome"}


@app.get("/menus", tags=["users"])
def get_menus():
    return {"menus": "menu1"}


@app.get("/users", tags=["menus"])
def get_users():
    return {"user": "user1"}
