def firstBadVersion(self, n):
    i, j = 0, n
    earliest = n+1
    
    while i<=j:
        mid = i + (j-i)//2
        
        if isBadVersion(mid):
            earliest = min(mid, earliest)
            j = mid-1
        else:
            i = mid+1
    
    return earliest