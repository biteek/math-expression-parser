class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class Number(ASTNode):
    def __init__(self, value):
        self.value = float(value)

class Variable(ASTNode):
    def __init__(self, name):
        self.name = name

class BinOp(ASTNode):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Assignment(ASTNode):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr