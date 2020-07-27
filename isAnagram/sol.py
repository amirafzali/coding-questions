def isAnagram(self, s, t):
    if len(s) != len(t): return False
    if not s: return True

    found = Counter(s)
    
    for char in t:
        if char not in found or found[char] == 0:
            return False
        found[char]-=1
            
    return sum(found.values) == 0