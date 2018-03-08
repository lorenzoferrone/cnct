from parser import Parser
from transformer import Transformer
from std import env
import sys, os, time, pickle
import re
from copy import deepcopy
from std.utility import popn


def loadFile(path):
    f = open(path, 'r')
    code = "".join(f.readlines())
    return code


def preprocessCode(code):
    '''serve per trattare i numeri negativi, non trovo altro modo -,-'''
    r = re.compile(r"-([\d]+)")
    return re.sub(r, '0 \\1 -', code, 0)


def loadModule(name, path, parser=None):
    moduleFile = path + '/' + name
    moduleCode = loadFile(moduleFile)
    executeFromString(moduleCode, parser, main=False)


def parse_list(token):
    def _(stack_, token=token):
        return execute(token.tail, stack_)
    return _


def execute(tokens, stack=None, currentEnv=env, path=None, parser=None):
    if stack is None: stack = []
    # if currentEnv is None: currentEnv = env
    for token in tokens:
        if token.head == 'import_stmt':
            name = "".join(token.tail[0].tail)
            loadModule(name, path, parser=parser)

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

            def _(stack_, token=token):
                if type(token.tail[1]) != list:
                    params = token.tail[1]
                    for par in reversed([par.tail[0] for par in params.tail]):
                        value = stack_.pop()
                        env[par] = value    
                    return execute(token.tail[2], stack_)
                else:
                    return execute(token.tail[1], stack_)

            _.__name__ = name
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
            try:
                value = env[token.tail[0]]
            except KeyError as error:
                print ('Error:', token.tail[0], 'is undefined')
                sys.exit(1)
                
            try:
                # va sistemato un po sto punto
                stack = value(stack)
            except TypeError as error:
                stack.append(value)
            except UnboundLocalError as error:
                pass

        if token.head == 'string':
            stack.append(token.tail[0][1:-1])

        if token.head == 'list':
            # def _(stack_, token=token):
            #     return execute(token.tail, stack_)
            stack.append(parse_list(token))

        if token.head == 'array':
            stack.append(execute(token.tail, []))
        
        if token.head == 'concat':
            res = []
            for func in token.tail:
                l_old = len(stack)
                stack = parse_list(func)(stack)
                l_new = len(stack)
                # non posso poppare un solo elemento, devo poppare tutti quelli nuovo calcolati
                # può capitare anche che lo stack sia più corto di prima!
                # devo trovare un modo per far capire quanti sono i valori tornati da func
                arity = ...
                if arity == 1:
                    res.append(stack.pop())
                else:
                    res.extend(popn(stack, arity))
            stack.extend(res)

    return stack


def executeFromString(code, parser, path=os.getcwd(), main=True, stack=None):
    # parsing:
    ast = parser(code)
    # seconda parte, piccole ulteriori modifiche
    trans = Transformer()
    ast = trans(ast)
    print (ast)
    # esecuzione dello stack
    stack = execute(ast, path=path, stack=stack, parser=parser)
    
    if main:
        print (stack)
    
    return stack


    

if __name__ == "__main__":

    start = time.time()
    grammarFile = 'grammars/JJ.g'
    parser = Parser(grammarFile)
    print ('loading time:', round(time.time() - start, 2), 's')
    
    # f = open('grammars/compiledGrammar.g', 'wb')
    # pickle.dump(parser.builtGrammar, f, 2)
    # f.close()
    # 
    # f = open('grammars/compiledGrammar.g', 'rb')
    # pickle.load(f)
    # 
    
    programFile, *args = sys.argv[1:]
    path = programFile.split('/')[-2]
    
    # carico il codice da file, se uso il flag -x invece
    # leggo da riga di comando
    if programFile != '-x':
        code = loadFile(programFile)
        code = preprocessCode(code)
    else:
        code = args[0]
        code = preprocessCode(code)

    executeFromString(code, parser, path=path, main=True)