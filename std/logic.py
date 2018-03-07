from std.utility import popn
from std import addToEnv, stackify, env


@addToEnv('and')
@stackify
def and_(a, b): return a and b


@addToEnv('or')
@stackify
def or_(a, b): return (a or b)


@addToEnv('not')
@stackify
def n(a): return not a


@addToEnv('xor')
@stackify
def xor(a, b): return (a or b) and not (a and b)

