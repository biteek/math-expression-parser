from ast_nodes import Program, Number, Variable, BinOp, Assignment

class Interpreter:
    def __init__(self):
        self.env = {}

    def eval(self, node):
        if isinstance(node, Program):
            last_val = None
            for stmt in node.statements:
                last_val = self.eval(stmt)
            return last_val

        elif isinstance(node, Number):
            return node.value

        elif isinstance(node, Variable):
            if node.name not in self.env:
                raise ValueError(f"Zmienna '{node.name}' nie została zdefiniowana.")

            return self.env[node.name]

        elif isinstance(node, Assignment):
            val = self.eval(node.expr)
            self.env[node.name] = val
            return val

        elif isinstance(node, BinOp):
            left_val = self.eval(node.left)
            right_val = self.eval(node.right)

            if node.op == '+':
                return left_val + right_val
            elif node.op == '-':
                return left_val - right_val
            elif node.op == '*':
                return left_val * right_val
            elif node.op == '/':
                if right_val == 0:
                    raise ZeroDivisionError("Błąd. Dzielenie przez zero!")
                return left_val / right_val
            elif node.op == '^':
                return left_val ** right_val