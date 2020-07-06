def maxSubArray(self, nums):
    if not nums: return -2147483648
    maximum = float('-inf')
    current = 0
    
    for i in range(len(nums)):
        num = nums[i]
        current+=num
        maximum = max(maximum, current)
        
        if current < 0: current = 0
    
    return maximum