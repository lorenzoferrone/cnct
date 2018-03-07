from loader import executeFromString
from parser import Parser
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory



if __name__ == '__main__':

    grammarFile = 'grammars/JJ.g'
    parser = Parser(grammarFile)
    
    history = []
    stack = []
    while True:
        code = prompt('>>> ', history=FileHistory('history.txt'))

        if code == 'quit':
            break
        elif code == '_':
            if history:
                stack = history[-1]
            else:
                stack = []
            print(stack)
        else:
            try:
                stack = executeFromString(code, parser, stack=stack)
                history.append(stack)
            except Exception as error:
                raise error
                continue
