def numDecodings(self, s):
    ways = [0 for i in range(len(s)+1)]
    ways[0] = 1
    ways[1] = 1 if s[0] != '0' else 0

    for i in range(1,len(s)):
        if s[i] != '0':
            ways[i+1] += ways[i]
            
        if 10 <= int(s[i-1:i+1]) <= 26:
            ways[i+1] += ways[i-1]
            
    return ways[-1]

def numDecodings(self, s):
    f = 1
    se = 1 if s[0] != '0' else 0

    for i in range(1,len(s)):
        new = 0
        if s[i] != '0':
            new += se
            
        if 10 <= int(s[i-1:i+1]) <= 26:
            new += f
            
        f = se
        se = new
            
    return se