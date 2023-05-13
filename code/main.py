from fastapi import FastAPI

from code.users import routers as user_routers


app = FastAPI()

app.include_router(user_routers.router)
