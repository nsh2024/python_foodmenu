from fastapi import FastAPI
from routers import users
from routers import menus
from config.config import settings

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

app.include_router(users.router)
app.include_router(menus.router)


@app.get("/", tags=[])
def index():
    return {"message": "welcome"}
