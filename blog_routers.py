from fastapi import APIRouter, Body
from pydantic import HttpUrl

import schemas

blog_router = APIRouter(
    prefix='/blogs',
    tags=['blogs']
)


@blog_router.post('/')
async def create_blog(url: HttpUrl, user: schemas.CreateUser = Body(...)):  # добавили в Body одно поле
    return {'url': url}
