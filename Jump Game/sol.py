def canJump(self, nums):
    if len(nums) <= 1: return True
    pos = len(nums)-1
    
    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] >= pos: pos = i
            
    return pos == 0