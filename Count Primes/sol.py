def countPrimes(self, n):
    if n <= 2: return 0
    found = set(i for i in range(3,n,2))
    found.add(2)
    
    for i in range(3, int(n**0.5)+1):
        if i not in found: continue
        for j in range(i+i, n, i):
            if j in found: found.remove(j)

    return len(found)