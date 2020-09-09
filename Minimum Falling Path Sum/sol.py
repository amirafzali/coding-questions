def minFallingPathSum(self, A):
    for i in range(len(A)-2,-1,-1):
        for j in range(len(A[i])-1, -1, -1):
            if j == len(A[i])-1:
                A[i][j]+= min(A[i+1][j], A[i+1][j-1])
            elif j == 0:
                A[i][j]+= min(A[i+1][j], A[i+1][j+1])
            else:
                A[i][j]+= min(A[i+1][j], A[i+1][j+1], A[i+1][j-1])
                
    return min(A[0])