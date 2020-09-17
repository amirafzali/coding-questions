def dieSimulator(self, n, rollMax):
    mem = {}
    
    def search(last,times,n):
        if n == 0: return 1
        
        if (last,times,n) in mem:
            return mem[(last,times,n)]
        
        total = 0
        for i in range(len(rollMax)):
            if i==last and times < rollMax[i]:
                total += search(i,times+1,n-1)
            elif i!=last:
                total += search(i,1,n-1)
                
        mem[(last,times,n)] = total
        return total
    
    res = search(-1,0,n)
    
    return res%(10**9+7)