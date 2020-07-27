def spiralOrder(self, matrix):
    if not matrix: return []
    res = []
    
    sC, eC, sR, eR = 0, len(matrix[0])-1, 0, len(matrix)-1
    
    while sC <= eC and sR <= eR:
        
        for i in range(sC, eC+1):
            res.append(matrix[sR][i])
        
        for i in range(sR+1, eR+1):
            res.append(matrix[i][eC])
            
        for i in range(eC-1, sC, -1):
            if sR == eR: break
            res.append(matrix[eR][i])
        
        for i in range(eR, sR, -1):
            if sC == eC: break
            res.append(matrix[i][sC])
            
        sC+=1
        eC-=1
        sR+=1
        eR-=1
            
    return res