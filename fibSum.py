def fibonacciSum(n):
    a = 1
    b = 1
    res = []
    while True:
        c = a+b
        if c>n:
            break
        a=b
        b=c
        res.append(c)
    import itertools
    for i in range(1,len(res)+1):
        for c in itertools.combinations(res, i):
            if sum(c) == n:
                return list(c)


print(fibonacciSum(21))