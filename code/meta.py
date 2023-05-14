import datetime as dt
import uuid

import ormar
from code import database


class BaseMeta(ormar.ModelMeta):
    metadata = database.metadata
    database = database.database


class User(ormar.Model):
    id = ormar.UUID(primary_key=True, default=uuid.uuid4)
    username = ormar.String(max_length=255, unique=True)
    first_name = ormar.String(max_length=255)
    last_name = ormar.String(max_length=255)
    created_at = ormar.DateTime(default=dt.datetime.now)
    updated_at = ormar.DateTime(default=dt.datetime.now)

    class Meta(BaseMeta):
        tablename = 'users'
