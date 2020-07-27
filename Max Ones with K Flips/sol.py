def longestOnes(self, A, K):
    longest = flips = i = 0
    
    for j in range(len(A)):
        if A[j] == 0:
            if flips == K:
                while A[i] != 0:
                    i+=1
                i+=1
            else:
                flips+=1
        longest = max(longest, j-i+1)
    
    return longest