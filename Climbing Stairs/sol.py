def climbStairs(self, n):
    f, l = 1, 2
    if n == 1: return 1
    
    for i in range(n-2):
        copy = l
        l = f + l
        f = copy
        
    return l