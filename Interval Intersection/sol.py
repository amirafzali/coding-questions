def intervalIntersection(self, A, B):        
    p1 = p2 = 0
    
    res = []
    
    while p1 < len(A) and p2 < len(B):
        print(p1,p2)
        res_start = max(A[p1][0],B[p2][0])
        res_end = min(A[p1][1],B[p2][1])
        if res_start <= res_end:
            res.append([res_start,res_end])
        
        if A[p1][1] <= B[p2][1]:
            p1+=1
        else:
            p2+=1
    
    return res