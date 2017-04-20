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
