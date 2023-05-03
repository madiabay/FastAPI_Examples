import uuid
from enum import Enum
from typing import Annotated

from fastapi import FastAPI, Path, Query, Body, Header, status, Form, UploadFile, File
from pydantic import HttpUrl

import schemas
import constants


app = FastAPI()

users = []

class UserFirstName(str, Enum):
    adik = 'adik'
    madi = 'madi'
    kayrat = 'kayrat'


@app.get('/calc/{num1}+{num2}')
def hello_world(
    num1: Annotated[int, Path(...)],
    num2: int = Path(...),
    num3: int = Query(None, alias='num_____3', deprecated=True, ge=5, include_in_schema=False)
):
    if not num3:
        num3 = 5
    return {'result': num1+num2+num3}


@app.post('/users/', tags=['users'], deprecated=False, status_code=status.HTTP_201_CREATED)
async def create_user(
    # locale: Annotated[constants.LocaleType, Header(..., alias='Accept-Language')],
    user: schemas.CreateUser = Body(
        ...,
        alias='user',
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "first_name": "string",
                    "last_name": "string",
                    "email": "user@example.com",
                    "gender": "MALE",
                    "wallets": [
                      {
                        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "currency": "KZT",
                        "amount": 12
                      }
                    ],
                    "password": "string"
                },
            },
            "invalid": {
                "summary": "A invalid example",
                "description": "A **invalid** item works incorrectly.",
                "value": {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "first_name": "string",
                    "last_name": "string",
                    "email": "user@example.com",
                    "gender": "MALE",
                    "wallets": [
                      {
                        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "currency": "KZT",
                        "amount": 0
                      }
                    ],
                    "password": "string"
                },
            },
        }
    )
) -> schemas.User:
    users.append(user)
    return user


@app.post('/users/{user_id}', tags=['users'], deprecated=False)
async def update_user(
    user_id: uuid.UUID,
    new_user: schemas.CreateUser = Body(..., alias='user')
) -> schemas.User:
    user_index = next((i for i, u in enumerate(users) if u.id == user_id), None)
    print(user_index)

    print('data: ', new_user.dict(exclude_unset=True, exclude_none=True))


    return new_user


@app.post('/blogs')
async def create_blog(url: HttpUrl, user: schemas.CreateUser = Body(...)): # добавили в Body одно поле
    return {'url': url}


@app.post('/login')
async def login(username: str = Form(...), password: str = Form(...)):
    return {
        'username': username,
        'password': password
    }


@app.post('/file')
async def file(file: UploadFile = File(...)):
    return {'file_name': file.filename}
