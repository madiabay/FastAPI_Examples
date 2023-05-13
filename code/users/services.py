from typing import Protocol

from . import repos, schemas


class UserServiceInterface(Protocol):

    async def create_user(self) -> schemas.User: ...


class UserServiceV1:
    repo: repos.UserRepoInterface = repos.UserRepoV1()

    async def create_user(self) -> schemas.User:
        return await self.repo.create_user()
