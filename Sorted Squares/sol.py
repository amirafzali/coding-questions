def sortedSquares(self, A):
    i, j = 0, len(A)-1
    use = [num for num in A]
    
    while i <= j:
        val1, val2 = abs(A[i]), abs(A[j])
        
        if val1 > val2:
            use[j-i] = val1**2
            i+=1
        else:
            use[j-i] = val2**2
            j-=1
            
    return use