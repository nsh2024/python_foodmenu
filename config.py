class Settings:
    TITLE = "Weekly Menu Plan"
    VERSION = "1.0"
    DESCRIPTION = """
    This is a weekly Menu plan application, to create/update/list the menu plan for each day.
    """
    NAME = "Girish"
    EMAIL = "girish@bal.com"
    TAGS = [
        {
            "name": "users",
            "description": "All user related routes"
        },
        {
            "name": "menus",
            "description": "All menu related routes"
        }
    ]
    OPENAPI_URL = "/api/v1/openapi.json"
    DOCUMENTATION_URL = "/documentation"


settings = Settings()