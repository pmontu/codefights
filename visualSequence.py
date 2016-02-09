def visualSequence(r, n):
    i = 1
    while(i<n):
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
        r = s
        i+=1
    return r

print(visualSequence(12, 4))