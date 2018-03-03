from parser import Parser
from transformer import Transformer
from std import env
import sys
from plyplus.strees import STree


def loadFile(path):
    f = open(path, 'r')
    code = "".join(f.readlines())
    return code


def loadModule(name):
    pass

def execute(tokens, stack=None, currentEnv=env):
    if stack is None: stack = []

    # if currentEnv is None: currentEnv = env

    for token in tokens:

        if token.head == 'import_stmt':
            name = token.tail[0].tail[0]
            loadModule(name)

        if token.head == 'assign_stmt':
            type_ = token.tail[0].head
            names = [x.tail[0] for x in token.tail[0].tail]
            # print (names, type_, token.tail[0].tail)
            if type_ == 'assign_normal':
                values = stack[-len(names):]
                # print (values)
                for name, value in zip(names, values):
                    env[name] = value
            if type_ == 'assign_drop':

                for name in reversed(names):
                    value = stack.pop()
                    env[name] = value

            if type_ == 'assign_acc':
                # per il momento gli acc non possono avere liste come target
                value = stack[-1]
                try:
                    env[names[0]].append(value)
                except:
                    env[names[0]] = [value]

            if type_ == 'assign_acc_drop':
                # per il momento gli acc non possono avere liste come target
                value = stack.pop()
                try:
                    env[names[0]].append(value)
                except:
                    env[names[0]] = [value]

        if token.head == 'definition':
            name = token.tail[0].tail[0]

            # assign_stmt(assign_drop(name('f')))
            def _(stack_, token=token):
                if type(token.tail[1]) != list:
                    params = token.tail[1]
                    for par in [par.tail[0] for par in params.tail]:
                        value = stack_.pop()
                        env[par] = value
                
                    
                    return execute(token.tail[2], stack_)
                else:
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
    print ('\n\n\n')

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
