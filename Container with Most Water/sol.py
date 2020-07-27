def maxArea(self, height):
    p1, p2 = 0, len(height)-1
    greatest = 0
    
    while p1 < p2:
        basis = min(height[p1], height[p2])
        greatest = max(greatest, basis*(p2-p1))
        if height[p2] > height[p1]: p1+=1
        else: p2-=1
            
    return greatest