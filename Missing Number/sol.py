def missingNumber(self, nums):
    req = 0
    for i in range(1,len(nums)+1): req+=i
    have = sum(nums)
    
    for i in range(len(nums)+1):
        if have+i == req: return i
    
    return -1