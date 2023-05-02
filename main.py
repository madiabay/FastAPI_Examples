import uuid
from enum import Enum

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserFirstName(str, Enum):
    adik = 'adik'
    madi = 'madi'
    kayrat = 'kayrat'


class User(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    first_name: str = 'Madi'
    last_name: str
    email: EmailStr


@app.get('/calc/{num1}+{num2}')
def hello_world(
    num1: int = Path(...),
    num2: int = Path(...),
    num3: int = Query(None, alias='num_____3', deprecated=True, ge=5, include_in_schema=False)
):
    if not num3:
        num3 = 5
    return {'result': num1+num2+num3}


@app.post('/users/{name}', response_model=User, tags=['users'], deprecated=True)
async def bye(name: UserFirstName, user: User = Body(..., embed=True)):
    user.first_name = name
    print(user.dict())
    print(user.json())
    return user
