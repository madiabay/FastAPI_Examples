import uuid
from enum import Enum
from typing import Annotated

from fastapi import FastAPI, Path, Query, Body, Header

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


@app.post('/users/', tags=['users'], deprecated=False)
async def create_user(
    # locale: Annotated[constants.LocaleType, Header(..., alias='Accept-Language')],
    user: schemas.CreateUser = Body(..., alias='user')
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
