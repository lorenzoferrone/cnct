from std.utility import popn
from std import addToEnv, stackify, env
import math
from itertools import product



@addToEnv('*')
@stackify
def mult(a, b): return a * b

@addToEnv('/')
@stackify
def div(a, b): return b / a

@addToEnv('%')
@stackify
def mod(a, b): return b % a

@addToEnv('+')
@stackify
def sum(a, b): return a + b

@addToEnv('-')
@stackify
def sub(a, b): return b - a

@addToEnv('**')
@stackify
def power(a, b): return b ** a


@addToEnv('sqrt')
@stackify
def sqrt_(a): return math.sqrt(a)


@addToEnv('int')
@stackify
def int_(a): return int(a)

@addToEnv('str')
@stackify
def str_(a): return str(a)

# comparison
@addToEnv('=')
@stackify
def equal(a, b): return a == b

@addToEnv('!=')
@stackify
def neq(a, b): return a != b

@addToEnv('<=')
@stackify
def le(a, b): return b <= a

@addToEnv('>=')
@stackify
def ge(a, b): return b >= a

@addToEnv('<')
@stackify
def le(a, b): return b < a

@addToEnv('>')
@stackify
def ge(a, b): return b > a

@addToEnv('!')
@stackify
def n(a): return not a

@addToEnv('and')
@stackify
def and_(a, b): return a and b

@addToEnv('or')
@stackify
def or_(a, b): return (a or b)

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
