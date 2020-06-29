def zigzagTraverse(matrix):
        if not matrix: return []
        n, m = len(matrix), len(matrix[0])
        i, j = 0, 0
        res = []
        down = True
    
        while 0<=i<n and 0<=j<m:
            res.append(matrix[i][j])
            if down:
                if i == n-1:
                    j+=1
                    down = False
                elif j==0:
                    i+=1
                    down = False
                else :
                    i+=1
                    j-=1  
            else:
                if j==m-1:
                    i+=1
                    down = True
                elif i==0:
                    j+=1
                    down = True
                else:
                    i-=1
                    j+=1
                
        return res