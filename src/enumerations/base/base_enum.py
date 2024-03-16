from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def values(cls) -> list[str]:
        return [item.value for item in cls]

    @classmethod
    def valid_value(cls, value: str) -> bool:
        return value in cls.values()

    def __str__(self) -> str:
        return self.value
