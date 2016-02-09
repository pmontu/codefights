def isPrime(i):
    prime = True
    for j in range(2,i):
        if i % j ==0:
            prime = False
    return prime

def primeFactors2(n):
    ans = []
    if n > 1:
        for i in range(2, int(n/2)+1):
            if n % i ==0:
                prime = isPrime(i)
                if prime:
                    ans.append(i)
        if isPrime(n):
            ans.append(n)
    return ans

for i in range(100):
    print(i, primeFactors2(i))

print(primeFactors2(2))