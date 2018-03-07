from std.utility import popn
from std import addToEnv, stackify, env

import math
from itertools import product


@addToEnv('@')
def take_index(stack):
    num, l = popn(stack, 2)
    if type(num) == list:
        stack.append(l[num[0]:num[1]])    
    else:
        stack.append(l[num])
    return stack

@addToEnv('range')
def range_(stack):
    x = stack.pop()
    x = int(math.ceil(x))
    stack.append(list(range(x)))
    return stack
    

@addToEnv('interval')
def interval(stack):
    x, y = popn(stack, 2)
    x = int(math.ceil(x))
    y = int(math.ceil(y))
    stack.append(list(range(y, x + 1)))
    return stack


@addToEnv('append')
def append(stack):
    num, l = popn(stack, 2)
    l.append(num)
    stack.append(l)
    return stack   
    
    
@addToEnv('len')
def length(stack):
    stack.append(len(stack.pop()))
    return stack


@addToEnv('in')
def in_(stack):
    l, num = popn(stack, 2)
    stack.append(num in l)
    return stack


    
@addToEnv('cross')
@stackify
def cross(l1, l2):
    return list(map(list, product(l1, l2)))

    
@addToEnv('kfold')
@stackify
def kfold(n, l1):
    return list(map(list, product(l1, repeat=n)))

    
@addToEnv('permutation')
@stackify
def permute(n, l1):
    return list(map(list, product(l1, repeat=n)))


@addToEnv('max')
@stackify
def max_(l): return max(l)


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


@addToEnv('remove')
def remove(stack):
    n, l = popn(stack, 2)
    value = l.pop(n)
    stack.append(l)
    stack.append(value)
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