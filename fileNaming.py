def fileNaming(n):
    i =1
    d = {}
    #len(n)
    while(i<4):
        def do(ni):
            if i == 3:
                print("in", ni, n[:i])
            if ni in n[:i]:
                if ni in d:
                    d[ni] += 1
                else:
                    d[ni] = 1
                new = "{0}({1})".format(ni, d[ni])
                if new in n[:i]:
                    do(new)
                else:
                    print("..",new)
                    return new
            return ni
        ans = do(n[i])
        if i == 3:
            print("--", ans)
        n[i] = ans
        i+=1
    return n


# print((fileNaming(["doc", "doc", "image", "doc(1)", "doc"])))
print(fileNaming(["a(1)", 
 "a(6)", 
 "a", 
 "a", 
 "a", 
 "a", 
 "a", 
 "a", 
 "a", 
 "a", 
 "a", 
 "a"]))