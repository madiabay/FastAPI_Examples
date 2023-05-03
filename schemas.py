import uuid
from decimal import Decimal

from pydantic import BaseModel, EmailStr, Field, validator

import constants


class Wallet(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    currency: constants.WalletCurrency
    amount: Decimal = Field(max_digits=14, decimal_places=2, gt=0)


class User(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    first_name: str | None = Field(None, min_length=1)
    last_name: str
    email: EmailStr
    gender: constants.GenderType
    wallets: list[Wallet] = Field(min_items=1)

    # @validator('first_name')
    # def first_name_must_starts_with_a(cls, value: str, values: dict):
    #     if not value.lower().startswith('a'):
    #         raise ValueError('first_name не может начинаться буквой а')
    #     return value

    @validator('wallets', each_item=True)
    def wallets_item_must_gt_0(cls, wallet: Wallet):
        if wallet.amount <= 0:
            raise ValueError('value must be greater than 0')
        return wallet

    # @validator('wallets')
    # def wallets_length_gt_3(cls, value):
    #     assert len(value) > 3, f'{value} length is not gt than 3'
    #     return value


class CreateUser(User):
    password: str
