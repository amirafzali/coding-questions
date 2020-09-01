def romanToInt(self, s):
    lookup = {'I': 1,'V':5,'X':10,'L': 50,'C':100,'D':500,'M':1000}
    if not s: return 0
    if len(s) == 1: return lookup[s[0]]
    total = lookup[s[-1]]
    
    for i in range(len(s)-2,-1,-1):
        if lookup[s[i]] < lookup[s[i+1]]:
            total-=lookup[s[i]]
        else:
            total+=lookup[s[i]]
            
    return total