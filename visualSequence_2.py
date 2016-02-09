def g(r):
    l = list(str(r))
    k = 1
    f = l[0]
    c = 1
    s = ""
    while(k<len(l)):
        if f == l[k]:
            c+=1
        else:
            s += "{0}{1}".format(c,f)
            c = 1
            f = l[k]
        k+=1
    if c>0:
        s += "{0}{1}".format(c,f)
    return s

def visualSequence(r, n):
    i = 1
    while(i<n):
        r = g(r)
        i+=1
    return r

print(visualSequence(1112211, 4))