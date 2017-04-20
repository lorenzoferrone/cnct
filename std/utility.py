#utils functions
def popn(l, n):
    if n == 1:
        return l.pop()
    else:
        #vengono ritornati nell'ordine inverso
        # quindi se lo stack è [a, b, c] e faccio x, y = popn(stack, 2)
        # avrò x = c; y = b
        return [l.pop() for _ in range(n)]

def peekn(l, n):
    if n == 1:
        return l.pop()
    else:
        #vengono ritornati nell'ordine inverso
        # quindi se lo stack è [a, b, c] e faccio x, y = popn(stack, 2)
        # avrò x = c; y = b
        return [l.pop() for _ in range(n)]
