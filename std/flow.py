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
    # se lo stack è [cond1, action1, action2]
    # esegue action1 se cond1 è true, senno action2
    # boolean, ifTrue, ifFalse = popn(stack, 3)
    ifFalse, ifTrue, boolean = popn(stack, 3)
    if boolean:
        stack = ifTrue(stack)
    else:
        stack = ifFalse(stack)

    return stack


@addToEnv('case')
def case(stack):
    # lo stack deve essere [..., ( (cond1, action1), (cond2, action2), ... (actionElse) ) ]
    list_of_conditions = stack.pop()
    for condition, action in list_of_conditions[:-1]:
        # print(condition, action)
        if condition:
            stack = action(stack)
            return stack

    last_action = list_of_conditions[-1]
    stack = last_action(stack)
    return stack
