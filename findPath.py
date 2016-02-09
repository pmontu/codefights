def findPath(m):
    f =  sum(m, [])
    pos =f.index(1)
    x, y, l=pos/3, pos%3, len(f)
    print(x,y,l)
    
    val =  1
    while(val<=l):
        try:
            none = True
            n = val + 1
            print("=",n,x,y)
            if x-1>=0 and m[x-1][y] == n:
                print(x-1, y ,m[x-1][y])
                x=x-1
                val += 1
                none = False
            elif m[x+1][y] == n:
                print(x+1, ym[x+1][y])
                x=x+1
                val += 1
                none = False
            elif y-1>0 and m[x][y-1] == n:
                print(x, y-1,m[x][y-1])
                y=y-1
                val += 1
                none = False
            elif m[x][y+1] == n:
                print(x, y+1,m[x][y+1])
                y=y+1
                val += 1
                none = False
        except Exception:
            if val == l:
                return True
            if none:
                return False
            else:
                print(x,y)


print(findPath([[1, 4, 5], [2, 3, 6]]))