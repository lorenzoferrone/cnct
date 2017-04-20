from loader import executeFromString



if __name__ == '__main__':

    grammarFile = 'grammars/JJ.g'

    history = []
    while True:
        code = input('>>> ')
        if code != 'quit':
            executeFromString(code, grammarFile)
        else:
            break
