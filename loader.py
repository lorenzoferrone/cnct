from parser import Parser
from transformer import Transformer
from std import env
import sys


def loadFile(path):
    f = open(path, 'r')
    code = "".join(f.readlines())
    return code


def loadModule(name):
    pass

def execute(tokens, stack=None):
    if stack is None: stack = []

    for token in tokens:

        if token.head == 'import_stmt':
            name = token.tail[0].tail[0]
            loadModule(name)

        if token.head == 'assign_stmt':
            name = token.tail[0].tail[0]
            value = stack.pop()
            env[name] = value
            # def _(stack_, value=value):
            #     return execute([value], stack_)

            # env[name] = _

        if token.head == 'definition':
            name = token.tail[0].tail[0]
            def _(stack_, token=token):
                body = token.tail[1]
                return execute(token.tail[1], stack_)

            env[name] = _

        if token.head == 'int':
            stack.append(int(token.tail[0]))

        if token.head == 'float':
            stack.append(float(token.tail[0]))

        if token.head == 'bool':
            if token.tail[0] == 'True':
                stack.append(True)
            else:
                stack.append(False)

        if token.head == 'name':
            # da aggiungere parsing per i nomi col punto (importo da moduli)
            try:
                value = env[token.tail[0]]
            except KeyError:
                print ('Error:', token.tail[0], 'is undefined')
                sys.exit(0)
            try:
                # va sistemato un po sto punto
                stack = value(stack)
            except TypeError:
                stack.append(value)

        if token.head == 'string':
            stack.append(token.tail[0][1:-1])

        if token.head == 'list':
            def _(stack_, token=token):
                return execute(token.tail, stack_)
            stack.append(_)

        if token.head == 'array':
            stack.append(execute(token.tail, []))

    return stack


def executeFromString(code, grammarFile):
    # parsing:
    # prima parte
    parser = Parser(grammarFile)
    ast = parser(code)
    print (ast)

    # seconda parte, piccole ulteriori modifiche
    trans = Transformer()
    ast = trans(ast)
    # print ('secondasd', ast)

    # esecuzione dello stack
    stack = execute(ast)

    print ('\nfinal stack:')
    print (stack)



if __name__ == "__main__":

    grammarFile = 'grammars/JJ.g'

    programFile, *args = sys.argv[1:]
    # carico il codice da file, se uso il flag -x invece
    # leggo da riga di comando
    if programFile != '-x':
        code = loadFile(programFile)
    else:
        code = args[0]

    executeFromString(code, grammarFile)
