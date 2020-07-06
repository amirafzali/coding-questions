def threeSum(self, nums):    
    res = []
    if len(nums) <= 2: return res
    nums.sort()
    
    for i in range(len(nums)-2):
        j,k = i+1, len(nums)-1
        if i > 0 and nums[i] == nums[i-1]: continue
        while j < k:
            current = nums[i]+nums[j]+nums[k]
            if k < len(nums)-1 and nums[k] == nums[k+1]: 
                k-=1
                continue

            if current == 0:
                res.append([nums[i],nums[j],nums[k]])
                j+=1
                k-=1
            elif current < 0:
                j+=1
            else:
                k-=1
    
    return res