from src.interpreter import Interpreter
from src.lexer import Lexer
from src.token import Token
from src.parser_ import Parser


def _run(code: str) -> tuple[list[Token], list[Token]]:
    lexer = Lexer(code)
    tokens = lexer.generate_tokens()

    tokens_list = list(tokens)

    parser = Parser(tokens_list)
    tree = parser.parse()

    if not tree:
        return [], []

    interpreter = Interpreter()
    res = interpreter.visit(tree)

    return res, tokens_list


def run(code: str, debug=True) -> list[Token]:
    if debug:
        res, tokens_list = _run(code)
        print(tokens_list)
        return res
    else:
        try:
            return _run(code)[0]
        except Exception as e:
            print(e)
            return []
