from src.token import Token, TokenType


class Lexer:
    def __init__(self, text: str):
        self.text = iter(text)
        self.advance()

    def advance(self) -> None:
        self.current_char = next(self.text, None)

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()

            elif self.current_char.isdigit() or self.current_char == ".":
                yield self.generate_number()

            elif self.current_char == "+":
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == "-":
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == "*":
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == "/":
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == "^":
                self.advance()
                yield Token(TokenType.POW)
            elif self.current_char == "%":
                self.advance()
                yield Token(TokenType.MOD)

            elif self.current_char == "(":
                self.advance()
                yield Token(TokenType.LPAREN)

            elif self.current_char == ")":
                self.advance()
                yield Token(TokenType.RPAREN)

            else:
                raise Exception(f"Illegal character: {self.current_char}")

    def generate_number(self) -> Token:
        number_str = ""
        decimal_count = 0

        while self.current_char is not None and (
            self.current_char == "." or self.current_char.isdigit()
        ):
            if self.current_char == ".":
                decimal_count += 1
                if decimal_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        if number_str.startswith("."):
            number_str = "0" + number_str
        if number_str.endswith("."):
            number_str += "0"

        return Token(TokenType.NUMBER, float(number_str))
