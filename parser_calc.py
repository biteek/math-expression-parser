from lark import Lark, Transformer, v_args
from ast_nodes import Program, Number, Variable, BinOp, Assignment

# GRAMATYKA
calc_grammar = """
?start:program

program: statement*

?statement: assignment
            | expr

assignment: CNAME "=" expr

?expr: term
    | expr "+" term -> add
    | expr "-" term -> sub

?term: pow
    | term "*" pow -> mul
    | term "/" pow -> div

?pow: factor
    | factor "^" pow -> pow

?factor: NUMBER -> number
        | CNAME -> var
        | "(" expr ")"

%import common.NUMBER
%import common.CNAME
%import common.WS
%ignore WS
"""

# TRANSFORMER
@v_args(inline=True)
class ASTBuilder(Transformer):
    def program(self, *statements):
        return Program(list(statements))

    def add(self, left, right):
        return BinOp('+', left, right)

    def sub(self, left, right):
        return BinOp('-', left, right)

    def mul(self, left, right):
        return BinOp('*', left, right)

    def div(self, left, right):
        return BinOp('/', left, right)

    def pow(self, left, right):
        return BinOp('^', left, right)

    def number(self, val):
        return Number(val)

    def var(self, name):
        return Variable(str(name))

    def assignment(self, name, expr):
        return Assignment(str(name), expr)

def get_parser():
    return Lark(calc_grammar, parser='lalr', transformer=ASTBuilder())