from std.utility import popn
from std import addToEnv, env

@addToEnv('reduce')
def reduce_(stack):
    f, l = popn(stack, 2)
    while l:
        l = f(l)
        if len(l) == 1:
            break

    stack.append(l[0])
    return stack


@addToEnv('map')
def map_(stack):

    f, l = popn(stack, 2)
    L = []
    for x in l:
        y = f([x])
        L.append(y[0])
    stack.append(L)

    return stack

@addToEnv('dountil')
def dountil(stack):
    f, l = popn(stack, 2)
    L = []
    for x in l:
        y = f([x])
        # y è uno stack (una lista), il cui ultimo elemento deve essere un bool
        boolean = y.pop()
        L.append(boolean)
        if boolean:
            break
    stack.append(L)

    return stack


@addToEnv('filter')
def filter_(stack):
    cond, l = popn(stack, 2)
    L = []
    for x in l:
        if cond([x])[0]:
            L.append(x)
    stack.append(L)
    return stack
