from src.token import Token, TokenType
from src.nodes import (
    AddNode,
    MinusNode,
    NumberNode,
    PlusNode,
    SubtractNode,
    MultiplyNode,
    DivideNode,
)


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = iter(tokens)
        self.advance()

    def advance(self) -> None:
        self.current_token = next(self.tokens, None)

    def raise_error(self):
        raise Exception(f"Invalid syntax")

    def expr(self) -> AddNode | SubtractNode:
        res = self.term()

        while self.current_token is not None and (
            self.current_token.type in (TokenType.PLUS, TokenType.MINUS)
        ):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                res = AddNode(res, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                res = SubtractNode(res, self.term())

        return res

    def term(self):
        res = self.factor()

        while self.current_token is not None and (
            self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE)
        ):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                res = MultiplyNode(res, self.factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                res = DivideNode(res, self.factor())

        return res

    def factor(self):
        tok = self.current_token

        if not tok:
            self.raise_error()

        match tok.type:
            case TokenType.LPAREN:
                self.advance()
                res = self.expr()

                if not self.current_token:
                    self.raise_error()

                if self.current_token.type != TokenType.RPAREN:
                    self.raise_error()

                self.advance()
                return res

            case TokenType.NUMBER:
                self.advance()
                return NumberNode(tok.value)

            case TokenType.PLUS:
                self.advance()
                return PlusNode(self.factor())

            case TokenType.MINUS:
                self.advance()
                return MinusNode(self.factor())

            case _:
                self.raise_error()

    def parse(self):
        if self.current_token is None:
            return None

        res = self.expr()

        if self.current_token is not None:
            raise Exception(f"Unexpected token: {self.current_token}")

        return res
