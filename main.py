from fastapi import FastAPI

app_description = """
## This is a weekly Menu plan application, to create/update/list the menu plan for each day.
"""
tags = [
    {
        "name": "users",
        "description": "All user related routes"
    },
    {
        "name": "menus",
        "description": "All menu related routes"
    }
]

app = FastAPI(title="Weekly Menu Plan",
              description=app_description,
              version="1.0",
              contact={
                  "name": ": Girish",
                  "email": "girish@bal.com"
              },
              openapi_tags=tags,
              openapi_url="/api/v1/openapi.json",
              docs_url="/documentation"
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
