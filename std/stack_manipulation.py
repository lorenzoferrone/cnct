from std.utility import popn
from std import addToEnv, env
from math import ceil
from copy import deepcopy


@addToEnv('last')
def last(stack):
    return [stack[-1]]

@addToEnv('print')
def print_(stack):
    print (stack)
    return stack

@addToEnv('printLast')
def printLast(stack):
    print (stack[-1])
    return stack

@addToEnv('drop')
def drop(stack):
    _ = stack.pop()
    return stack

@addToEnv('id')
def id(stack):
    return stack

@addToEnv('range')
def range_(stack):
    x = stack.pop()
    x = int(ceil(x))
    stack.append(list(range(x)))
    return stack

@addToEnv('interval')
def interval(stack):
    x, y = popn(stack, 2)
    x = int(ceil(x))
    y = int(ceil(y))
    stack.append(list(range(y, x + 1)))
    return stack

@addToEnv('lengthAll')
def lengthAll(stack):
    stack.append(len(stack))
    return stack

@addToEnv('len')
def length(stack):
    stack.append(len(stack.pop()))
    return stack

@addToEnv('dup')
def dup(stack):
    stack.append(stack[-1])
    return stack

@addToEnv('dupn')
def dup(stack):
    n = stack.pop()
    stack.extend(stack[-n:])
    return stack

# take the element in nth position in the stack
# and puts a copy on top of it. [1 take] is the same as "dup"
@addToEnv('take')
def resurrect(stack):
    n = stack.pop()
    stack.append(stack[-n])
    return stack

@addToEnv('switch')
def switch(stack):
    a, b = popn(stack, 2)
    stack.append(a)
    stack.append(b)
    return stack

# @addToEnv('bi2')
# def bi(stack):
#     f, g, arg1, arg2 = popn(stack, 4)
#     stack.append(arg1)
#     stack.append(arg2)
#     stack.append(f(stack))
#     stack.append(g(arg1, arg2))
#     return stack

@addToEnv('bi')
def bi(stack):
    f, g, arg = popn(stack, 3)
    # f is a function of a stack and return stack
    # in this way I access the real result
    res1 = g([arg])[0]
    res2 = f([arg])[0]
    stack.append(res1)
    stack.append(res2)
    return stack

@addToEnv('both')
def bii(stack):
    # for function which return one output
    f, g = popn(stack, 2)
    # aggiornare con deepcopy ovunque
    stack_ = deepcopy(stack)
    stack = f(stack)
    stack_ = g(stack_)
    # print ('ss', stack_)

    stack.append(stack_[-1])
    return stack

@addToEnv('bif')
def bif(stack):
    # for function which return one output
    stmt, cond = popn(stack, 2)
    stack_ = stack.copy()
    stack = cond(stack)
    if stack[-1]:
        stack = stmt(stack_)
        return stack
        # print ('stack_', stack_)
    else:
        return stack

@addToEnv('.')
def apply(stack):
    f = stack.pop()
    stack = f(stack)
    return stack

@addToEnv('all')
def all(stack):
    # for function which take n input and return one output
    funcList = popn(stack, 1)

    # la prima funzione la faccio fuori dal ciclo
    f = funcList[0]
    stack_ = deepcopy(stack)   # copy of the original stack
    stack = f(stack)
    results = []
    for f in funcList[1:]:
        stack__ = deepcopy(stack_)
        stack__ = f(stack__)
        results.append(stack__[-1])

    stack.extend(results)
    return stack


@addToEnv('pair')
def pair(stack):
    a, b = popn(stack, 2)
    stack.append([b, a])
    return stack

@addToEnv('group')
def group(stack):
    n = stack.pop()
    values = popn(stack, n)
    stack.append(list(reversed(values)))
    return stack

@addToEnv('reverse')
def reverse_(stack):
    l = stack.pop()
    # stack.append(l.reverse())
    stack.append(l[::-1])
    return stack

@addToEnv('unroll')
def unroll(stack):
    l = stack.pop()
    for x in l:
        stack.append(x)
    return stack

@addToEnv('zip')
def z(stack):
    l1, l2 = popn(stack, 2)
    stack.append(list(zip(l2, l1)))
    return stack

@addToEnv('any')
def any_(stack):
    l = stack.pop()
    stack.append(any(l))
    return stack

# @addToEnv('take')
# def take(stack):
#     n, l = popn(stack, 2)
#     stack.append(l[n])
#     return stack

@addToEnv('remove')
def remove(stack):
    n, l = popn(stack, 2)
    value = l.pop(n)
    stack.append(l)
    stack.append(value)
    return stack
