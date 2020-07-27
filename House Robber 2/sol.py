def rob(self, nums):
    if not nums: return 0
    if len(nums) <= 3: return max(nums)
    
    p1,p2 = nums[1], max(nums[1],nums[2])
    
    for i in range(3,len(nums)):
        p1, p2 = p2, max(p2, nums[i]+p1)
    
    greatest = p2
    p1,p2 = nums[0], max(nums[0],nums[1])
    
    for i in range(2,len(nums)-1):
        p1, p2 = p2, max(p2, nums[i]+p1)
        
        
    return max(greatest, p2)