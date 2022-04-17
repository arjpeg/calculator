from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    NUMBER = 0

    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    POW = 5
    MOD = 6

    LPAREN = 7
    RPAREN = 8


@dataclass
class Token:
    type: TokenType
    value: int | float | None = None

    def __repr__(self) -> str:
        return f'{self.type.name}{f":{self.value}" if self.value is not None else ""}'
