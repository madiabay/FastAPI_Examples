import uuid
from typing import Protocol
from code.meta import User

from . import repos, schemas


class UserServiceInterface(Protocol):

    async def create_user(self, user: schemas.User) -> User: ...

    async def get_users(self) -> list[User]: ...

    async def update_user(self, pk: uuid.UUID, user: schemas.UpdateUser) -> User: ...


class UserServiceV1:
    repo: repos.UserRepoInterface = repos.UserRepoV1()

    async def create_user(self, user: schemas.User) -> User:
        return await self.repo.create_user(user=user)

    async def get_users(self) -> list[User]:
        return await self.repo.get_users()

    async def update_user(self, pk: uuid.UUID, user: schemas.UpdateUser) -> User:
        return await self.repo.update_user(pk=pk, user=user)
