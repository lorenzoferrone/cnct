from std.utility import popn
from std import addToEnv, stackify, env

@addToEnv('str')
@stackify
def str_(a): return str(a)