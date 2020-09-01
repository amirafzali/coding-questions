def frequencySort(self, s):
    if not s: return []
    freq = Counter(s)
    max_freq = max(freq.values())
    
    res = defaultdict(list)
    
    for char in freq.keys():
        res[freq[char]].append(char)
        
    to_return = []
    
    for i in range(max_freq,-1,-1):
        if i in res:
            for char in res[i]:
                to_return.append(char*i)
    
    return "".join(to_return)