def partitionLabels(self, S):
    lastIndex = {}
    res = []
    start = cut = 0
    
    for i in range(len(S)):
        lastIndex[S[i]] = i
    
    for i in range(len(S)):
        ch = S[i]
        cut = max(cut, lastIndex[ch])

        if i == cut:
            res.append(i-start+1)
            start = i+1
    
    return res