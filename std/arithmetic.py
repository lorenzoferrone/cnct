from std.utility import popn
from std import addToEnv, stackify, env
import math



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

@addToEnv('not')
@stackify
def n(a): return not a
