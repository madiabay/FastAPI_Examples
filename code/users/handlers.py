import uuid

from code.meta import User

from . import services, schemas


class UserHandler:
    service: services.UserServiceInterface = services.UserServiceV1()

    async def create_user(self, user: schemas.User) -> User:
        return await self.service.create_user(user=user)

    async def get_users(self) -> list[User]:
        return await self.service.get_users()

    async def update_user(self, pk: uuid.UUID, user: schemas.UpdateUser) -> User:
        return await self.service.update_user(pk=pk, user=user)
