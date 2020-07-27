def firstMissingPositive(self, nums):
    oneFound = False
    for i in range(len(nums)):
        if nums[i] <= 0:
            nums[i] = 1
        elif nums[i] == 1: oneFound = True
            
    if not oneFound: return 1
    
    for i in range(len(nums)):
        check = abs(nums[i])-1
        if 0 <= check < len(nums) and nums[check] > 0:
            nums[check]*=-1
            
    for i in range(len(nums)):
        if nums[i] > 0: return i+1
        
    return len(nums)+1