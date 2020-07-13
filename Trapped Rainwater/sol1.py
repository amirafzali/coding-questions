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