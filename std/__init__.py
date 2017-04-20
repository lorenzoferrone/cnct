from inspect import signature
from .utility import popn

def addToEnv(name):
    def real_decorator(function):
        env[name] = function
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
        return wrapper
    return real_decorator

# decorator for simple function which pop inputs from the stack
# and put the result onto it
def stackify(func):
    numParameters = len(signature(func).parameters)
    def newFunc(stack):
        args = popn(stack, numParameters)
        if numParameters == 1:
            result = func(args)
        else:
            result = func(*args)
        stack.append(result)
        return stack

    return newFunc


# lo definisco vuoto
env = {}

# dentro i moduli viene rimodificato, e poi lo reimporto
from .arithmetic import env
from .stack_manipulation import env
from .higher import env
from .flow import env
