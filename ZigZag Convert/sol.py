def convert(self, s, numRows):
    rows = min(len(s), numRows)
    store = [[] for i in range(rows)]
    
    if rows == 1: return s
    down = True
    current = 0
    
    for i in range(len(s)):
        store[current].append(s[i])
        
        if current==0: down=True
        elif current==rows-1: down=False
        
        if down: current+=1
        else: current-=1
            
    string = ""
    for row in store: string+="".join(row)
    return string