from src.interpreter import Interpreter
from src.lexer import Lexer
from src.token import Token
from src.parser_ import Parser


def run(code: str) -> list[Token]:
    try:
        lexer = Lexer(code)
        tokens = lexer.generate_tokens()

        tokens_list = list(tokens)

        parser = Parser(tokens_list)
        tree = parser.parse()

        if not tree:
            return []

        print(tree)

        interpreter = Interpreter()
        res = interpreter.visit(tree)

        print(res)
        return res

    except Exception as e:
        print(e)
        return []
