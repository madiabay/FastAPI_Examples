from typing import Annotated

from fastapi import Query, Depends, Header, HTTPException

from redis import asyncio as aioredis


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


class Connection:
    _redis = None

    @classmethod
    def redis(cls):
        if not cls._redis:
            cls._redis = aioredis.from_url('redis://localhost:6379')

        return cls._redis

    @classmethod
    async def close_redis(cls):
        if cls._redis:
            await cls._redis.close()
