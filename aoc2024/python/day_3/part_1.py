#!/usr/bin/env python3

import pathlib
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class TokenType(Enum):
    LEFT_PAREN = "LEFT_PAREN"
    COMMA = "COMMA"
    RIGHT_PAREN = "RIGHT_PAREN"
    MULTIPLY = "MULTIPLY"
    NUMBER = "NUMBER"

@dataclass
class Token:
    type: TokenType
    value: Optional[str] = None

def tokenize(program: str) -> iter:
    index: int = 0
    while index < len(program):
        char: str = program[index]
        
        if char == '(':
            yield Token(TokenType.LEFT_PAREN)
        elif char == ',':
            yield Token(TokenType.COMMA)
        elif char == ')':
            yield Token(TokenType.RIGHT_PAREN)
        elif char.isdigit():
            string: str = ''
            while program[index].isdigit():
                string += program[index]
                
                if program[index + 1].isdigit():
                    index += 1
                else:
                    break

            yield Token(TokenType.NUMBER, string)
        elif program[index:index + 3].casefold() == 'mul':
            yield Token(TokenType.MULTIPLY)
            index += 2
            
        index += 1

def evaluate(program: str) -> int:
    total: int = 0
    tokens = list(tokenize(program))
    
    for index, token in enumerate(tokens):
        if token.type != TokenType.MULTIPLY:
            continue
        
        left_parens, x, comma, y, right_parens = tokens[index+1:index+6]
        
        if left_parens.type != TokenType.LEFT_PAREN:
            continue
        
        if x.type != TokenType.NUMBER:
            continue
        
        if comma.type != TokenType.COMMA:
            continue
        
        if y.type != TokenType.NUMBER:
            continue
        
        if right_parens.type != TokenType.RIGHT_PAREN:
            continue
       
        total += int(x.value) * int(y.value)
        print(f'{x.value} * {y.value} = {int(x.value) * int(y.value)}')
        
    return total
        
        

program = pathlib.Path('input.txt').read_text()
print(evaluate(program))
