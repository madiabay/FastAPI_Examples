import uuid

from fastapi import APIRouter, Body, status

import schemas

user_router = APIRouter(
    prefix='/users',
    tags=['users']
)

users = []


@user_router.post('/', deprecated=False, status_code=status.HTTP_201_CREATED)
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


@user_router.patch('/{user_id}', deprecated=False)
async def update_user(
        user_id: uuid.UUID,
        new_user: schemas.CreateUser = Body(..., alias='user')
) -> schemas.User:
    user_index = next((i for i, u in enumerate(users) if u.id == user_id), None)
    print(user_index)

    print('data: ', new_user.dict(exclude_unset=True, exclude_none=True))

    return new_user
