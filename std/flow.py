from std.utility import popn
from std import addToEnv, env

@addToEnv('loop')
def loop(stack):
    times, stmt = popn(stack, 2)
    for i in range(times):
        stack = stmt(stack)

    return stack

@addToEnv('until')
def until(stack):
    cond, stmt = popn(stack, 2)
    stack_ = stack.copy()
    while cond(stack_)[-1]:
        stack = stmt(stack)
        stack_ = stack.copy()

    return stack[:-1]

@addToEnv('if')
def if_(stack):
    # se il top dello stack è true fai una cosa, senno un altra
    boolean, ifTrue, ifFalse = popn(stack, 3)
    if boolean:
        stack = ifTrue(stack)
    else:
        stack = ifFalse(stack)

    return stack
