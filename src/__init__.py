from src.interpreter import Interpreter
from src.lexer import Lexer
from src.token import Token
from src.parser_ import Parser


def _run(code: str) -> list[Token]:
    lexer = Lexer(code)
    tokens = lexer.generate_tokens()

    tokens_list = list(tokens)

    parser = Parser(tokens_list)
    tree = parser.parse()

    if not tree:
        return []

    interpreter = Interpreter()
    res = interpreter.visit(tree)

    return res


def run(code: str, debug=True) -> list[Token]:
    if debug:
        return _run(code)
    else:
        try:
            return _run(code)
        except Exception as e:
            print(e)
            return []
