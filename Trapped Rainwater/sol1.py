def trap(self, height):
    if not height: return 0
    left, right = [height[0]], [height[-1]]
    
    for i in range(1, len(height)):
        left.append(max(height[i], left[i-1]))
    
    for i in range(1, len(height)):
        curr = height[len(height)-i-1]
        right.append(max(curr, right[i-1]))
    
    total = 0
    
    for i in range(len(height)):
        use = min(left[i],right[len(height)-i-1])
        if use-height[i] > 0:
            total+= use-height[i]
            
    return total

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