
def solve(self, s, k):
    res = []

    if k < 0:
        k = -(abs(k)%26)
    else:
        k%=26
    
    for char in s:
        rep = ord(char)
            
        rep += k
        
        if rep < ord('a'):
            diff = ord('a')-rep
            res.append(chr(ord('z')-diff+1))
            
        elif rep > ord('z'):
            diff = rep - ord('z')
            res.append(chr(ord('a')+diff-1))
            
        else:
            res.append(chr(rep))
            
    return "".join(res)


def solve(self, l0, l1):
    rolling=0
    found = set()
    for num in l0:
        rolling+=num
        found.add(rolling)
        
    rolling=0  
    count = 0
    for num in l1:
        rolling+=num
        if rolling in found:
            count+=1
            
    return count