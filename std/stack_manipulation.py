from std.utility import popn
from std import addToEnv, env
from math import ceil
from copy import deepcopy


@addToEnv('last')
def last(stack):
    return [stack[-1]]
    
    
@addToEnv('clear')
def clear(stack):
    return []


@addToEnv('drop')
def drop(stack):
    _ = stack.pop()
    return stack


@addToEnv('lengthAll')
def lengthAll(stack):
    stack.append(len(stack))
    return stack


@addToEnv('dup')
def dup(stack):
    copy = deepcopy(stack[-1])
    stack.append(copy)
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
