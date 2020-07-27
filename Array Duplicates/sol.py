def findDuplicates(self, nums):
    res = []
    for i,num in enumerate(nums):
        use = abs(num)-1
        if nums[use] < 1: res.append(use+1)
        else: nums[use] = abs(nums[use])*-1
            
    return res