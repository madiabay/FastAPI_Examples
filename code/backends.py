from starlette.authentication import AuthenticationBackend, AuthCredentials, SimpleUser


class OurUser(SimpleUser):

    def __init__(self, username: str, name: str):
        self.name = name
        super().__init__(username)


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        # TODO: You'd want to verify the username and password here.
        return AuthCredentials(["authenticated"]), OurUser(username='madi123', name='madi')
