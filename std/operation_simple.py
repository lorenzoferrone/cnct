from utility import popn


# list
def take(stack):
    numero, lista = popn(stack, 2)
    stack.append(lista[numero])
    return stack

def n(stack):
    num, elem = popn(stack, 2)
    stack.append(num*[elem])
    return stack

def range_(stack):
    n = popn(stack, 1)
    stack.append(list(range(n)))
    return stack

def sort(stack):
    l = popn(stack, 1)
    stack.append(sorted(l))
    return stack

def reverse(stack):
    l = popn(stack, 1)
    stack.append(list(reversed(l)))
    return stack
