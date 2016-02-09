def PowLength(A, B, b):
    n = A**B
    c = 0
    while(True):
        if n < b:
            c+=1
            break
        else:
            c+=1
            n /= b
    return c

assert(PowLength(835, 835, 2) == len("{0:b}".format(835**835)))