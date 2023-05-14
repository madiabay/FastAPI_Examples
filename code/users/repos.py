import uuid
from typing import Protocol
from code.meta import User

from . import schemas


class UserRepoInterface(Protocol):

    async def create_user(self, user: schemas.User) -> User: ...

    async def get_users(self) -> list[User]: ...

    async def update_user(self, pk: uuid.UUID, user: schemas.UpdateUser) -> User: ...


class UserRepoV1:

    async def create_user(self, user: schemas.User) -> User:
        return await User.objects.create(**user.dict())

    async def get_users(self) -> list[User]:
        return await User.objects.all()

    async def update_user(self, pk: uuid.UUID, user: schemas.UpdateUser) -> User:
        await User.objects.filter(pk=pk).update(**user.dict(exclude_unset=True))

        return await User.objects.get(pk=pk)
