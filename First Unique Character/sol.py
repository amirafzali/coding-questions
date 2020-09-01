def firstUniqChar(self, s):
    lookup = Counter(s)
    
    for i,char in enumerate(s):
        if lookup[char] == 1: return i
    
    return -1