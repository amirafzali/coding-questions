def numSquares(self, n):
    lookup = []
    mem = {0:0}
    i = 1
    while i*i <= n:
        lookup.append(i*i)
        i+=1
        
        
    for i in range(1,n+1):
        mem[i] = float('inf')
        for j in lookup:
            if i >= j:
                mem[i] = min(mem[i], 1+mem[i-j])
            else:
                break
                
    return mem[n]