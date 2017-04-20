from plyplus import STransformer
from std import env


class AbstractInterpreter(STransformer):

    def __call__(self, ast):
        return self.transform(ast)


class Transformer(AbstractInterpreter):

    def __init__(self):
        pass

    # def string(self, expression):
    #     return expression

    def body(self, expression):
        return expression.tail

    def start(self, expression):
        return expression.tail

    # def punt(self, expression):
    #     return expression.tail[0]

    # def array(self, expression):
    #     return expression

    def __default__(self, expression):
        return expression
