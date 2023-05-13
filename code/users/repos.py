from typing import Protocol

from . import schemas


class UserRepoInterface(Protocol):

    async def create_user(self) -> schemas.User: ...


class UserRepoV1:

    async def create_user(self) -> schemas.User:
        return schemas.User(username='mado', first_name='madi', last_name='abay')
