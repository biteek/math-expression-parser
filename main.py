import sys
from lark.exceptions import UnexpectedInput
from parser_calc import get_parser
from interpreter import Interpreter

def execute_code(code_str, parser, interpreter):
    try:
        ast_tree = parser.parse(code_str)
        return interpreter.eval(ast_tree)
    except UnexpectedInput as e:
        print(f"Syntax error: nieoczekiwany token w linii {e.line}, kolumnie {e.column}.")
    except (ZeroDivisionError, ValueError) as e:
        print(e)
    return None

def main():
    parser = get_parser()
    interpreter = Interpreter()

    inputs = [
        "x = 5 + 3 * 2",
        "y = x ^ 2",
        "y / (x - 11)",
        "z = 10 + * 5",
        "10 / 0"
    ]

    for code in inputs:
        print(f"\nWejście: {code}")
        res = execute_code(code, parser, interpreter)
        if res is not None:
            print(f"Wynik: {res}")

if __name__ == "__main__":
    main()