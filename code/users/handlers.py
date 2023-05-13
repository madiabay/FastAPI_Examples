from . import services, schemas


class UserHandler:
    service: services.UserServiceInterface = services.UserServiceV1()

    async def create_user(self) -> schemas.User:
        return await self.service.create_user()
