from plyplus import Grammar

class Parser:
    def __init__(self, grammarPath):
        self.grammar = self.loadGrammar(grammarPath)
        self.builtGrammar = self.buildGrammar()

    @staticmethod
    def loadGrammar(path):
        f = open(path, 'r')
        return "".join(f.readlines())

    def parse(self, sentence):
        return self.builtGrammar.parse(sentence)

    def buildGrammar(self):
        return Grammar(self.grammar)


    def __call__(self, sentence):
        # parse either a string or an external file
        if isinstance(sentence, str):
            return self.parse(sentence)
        else:
            raise NotImplemented


if __name__ == "__main__":

    grammarFile = 'grammars/calc.g'
    P = Parser(grammarFile)

    sentence = "a = 5 + 6"

    ast = P(sentence)

    print (ast)
