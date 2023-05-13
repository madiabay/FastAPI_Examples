from enum import Enum


class WalletCurrency(Enum):
    KZT = 'KZT'
    USD = 'USD'
    RUB = 'RUB'


class GenderType(Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'


class LocaleType(Enum):
    ru = 'ru'
    kk = 'kk'
    en = 'en'
