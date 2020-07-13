def maxSubArray(self, nums):
    largest = nums[0]
    current = 0
    
    for i in range(len(nums)):
        current+=nums[i]
        largest = max(largest, current)
        if current < 0: current = 0
    
    return largest