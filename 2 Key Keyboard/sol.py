def minSteps(self, n):
    mem = {}
    def search(current):
        if current in mem: return mem[current]
        if current == 1: return 0
        
        shortest = float('inf')
        
        for i in range(2,current+1):
            if current%i == 0:
                shortest = min(shortest, i+search(current/i))
                
        mem[current] = shortest
        return shortest
    
    return search(n)