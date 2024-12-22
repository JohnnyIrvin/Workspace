#!/usr/bin/env python3

import pathlib
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class TokenType(Enum):
    LEFT_PAREN = 1
    COMMA = 2
    RIGHT_PAREN = 3
    MULTIPLY = 4
    NUMBER = 5

@dataclass
class Token:
    type: TokenType
    value: Optional[str] = None

def tokenize(program: str) -> iter:
    for index, char in enumerate(program):
        if char == '(':
            yield Token(TokenType.LEFT_PAREN)
        elif char == ',':
            yield Token(TokenType.COMMA)
        elif char == ')':
            yield Token(TokenType.RIGHT_PAREN)
        elif char == '*':
            yield Token(TokenType.MULTIPLY)
        elif char.isdigit():
            string: str = ''
            while program[index].isdigit():
                string += program[index]
                index += 1
            yield Token(TokenType.NUMBER, string)
            if program[index:index + 3].casefold() == 'mul':
                yield Token(TokenType.MULTIPLY)
                index += 3

program = pathlib.Path('sample.txt').read_text()
print(list(tokenize(program)))