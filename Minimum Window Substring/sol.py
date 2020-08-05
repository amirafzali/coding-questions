def minWindow(self, s, t):
    tFreq = Counter(t)
    unique = len(tFreq.values())
    
    window = {}
    seen = set()
    res = [0,float('inf')]
    i = 0
    
    for j in range(len(s)):
        char = s[j]
        window[char] = window.get(char,0)+1
        if char in tFreq and window[char] >= tFreq[char]:
            seen.add(char)
            
        while i <= j and (s[i] not in tFreq or window[s[i]] > tFreq[s[i]]):
            window[s[i]]-=1
            i+=1
        
        if len(seen) == unique:
            if j-i < res[1]-res[0]:
                res[0] = i
                res[1] = j

    if res[1]-res[0] > len(s):
        return ""
    else:
        return s[res[0]:res[1]+1]