def leftMostColumnWithOne(self, binaryMatrix):
    m, n = binaryMatrix.dimensions()
    lowest = float('inf')
    
    for i in range(m):
        low,high = 0,n-1
        
        while low<=high:
            mid = low + (high-low)//2
            elm = binaryMatrix.get(i,mid)
            
            if elm == 1: 
                lowest = min(lowest,mid)
                high = mid-1
            else:
                low = mid+1
        
    
    return -1 if lowest == float('inf') else lowest