from pydantic import BaseModel


class User(BaseModel):
    username: str
    first_name: str
    last_name: str


class UpdateUser(BaseModel):
    username: str | None
    first_name: str | None
    last_name: str | None
