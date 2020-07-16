def isAnagram(self, s, t):
    if len(s) != len(t): return False
    found = Counter(s)
    
    for char in t:
        if char not in found:
            return False
        elif found[char] == 0:
            return False
        else:
            found[char]-=1
            
    for val in found.values(): 
        if val!=0: return False
    return True