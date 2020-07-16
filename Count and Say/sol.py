def countAndSay(self, n):
    res = '1'
    for i in range(n-1):
        concat = []
        pos = j = 0
        while j < len(res):
            count = 1
            
            while j < len(res)-1 and res[j]==res[j+1]:
                count+=1
                j+=1

            concat.append(str(count))
            concat.append(str(res[j]))
            j+=1
            
        res = "".join(concat)
        
    return res