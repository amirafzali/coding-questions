def minWindow(self, s, t):
    i = j = 0
    lookup = Counter(t)
    freq = {}
    contained = set()
    short = [len(s),len(s)*3]
    
    while j < len(s):
        freq[s[j]] = freq.get(s[j],0)+1
        if s[j] in lookup and freq[s[j]] == lookup[s[j]]:
            contained.add(s[j])
        while i <= j and (s[i] not in lookup or freq[s[i]] > lookup[s[i]]):
            freq[s[i]]-=1
            i+=1
        
        if len(contained) == len(lookup) and j-i < short[1]-short[0]:
            short[0] = i
            short[1] = j
        
        j+=1
    
    return s[short[0]:short[1]+1]