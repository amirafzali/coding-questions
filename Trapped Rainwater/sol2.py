def trap(self, height):
    if not height: return 0
    i, j = 0, len(height)-1
    lmax, rmax = height[i], height[j]
    total = 0
    
    while i < j:
        l, r = height[i], height[j]
        if l < r:
            if l >= lmax: lmax = l
            else: total+=lmax-l
            i+=1
        else:
            if r >= rmax: rmax = r
            else: total+=rmax-r
            j-=1
    
    return total