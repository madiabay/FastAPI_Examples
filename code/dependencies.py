from typing import Annotated

from fastapi import Query, Depends, Header, HTTPException


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


class SpecificQuery:
    def __init__(self, limit: int = 10):
        self.limit = limit


class CommonQuery:
    def __init__(
            self,
            specific_query: SpecificQuery = Depends(),
            page_size: int = Query(8, ge=8),
            page: int = 1
    ):
        self.specific_query = specific_query
        self.page_size = page_size
        self.page = page
