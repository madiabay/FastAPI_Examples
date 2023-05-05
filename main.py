from enum import Enum
from typing import Annotated

from fastapi import FastAPI, Path, Query, status, Form, UploadFile, File, HTTPException, Depends

import dependencies

from blog_routers import blog_router
from user_routers import user_router


app = FastAPI(
    dependencies=[Depends(dependencies.verify_key)]
)

app.include_router(blog_router)
app.include_router(user_router)

users = []

class UserFirstName(str, Enum):
    adik = 'adik'
    madi = 'madi'
    kayrat = 'kayrat'


@app.get('/calc/{num1}+{num2}', dependencies=[Depends(dependencies.verify_token)])
def hello_world(
    num1: Annotated[int, Path(...)],
    num2: int = Path(...),
    num3: int = Query(None, alias='num_____3', ge=5, include_in_schema=False),
    common_query: dependencies.CommonQuery = Depends()
):
    if not num3:
        num3 = 5
    return {
        'result': num1+num2+num3,
        'page_size': common_query.page_size,
        'page': common_query.page,
        'limit': common_query.specific_query.limit,
    }


@app.post('/login')
async def login(username: str = Form(...), password: str = Form(...)):
    return {
        'username': username,
        'password': password
    }


@app.post('/file')
async def file(file: UploadFile = File(...)):
    if file.filename != 'trump.png':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid image name')
    return {'file_name': file.filename}
