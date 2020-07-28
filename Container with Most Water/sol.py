def maxArea(self, height):
    greatest = float('-inf')
    i, j = 0, len(height)-1
    
    while i<j:
        greatest = max(greatest, min(height[i],height[j])*(j-i))
        if height[i] < height[j]: i+=1
        else: j-=1
            
    return greatest