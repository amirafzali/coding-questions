def productExceptSelf(self, nums):
    res = [1]
    for i in range(1,len(nums)):
        res.append(res[-1]*nums[i-1])
    
    prod = 1
    for j in range(len(nums)-2,-1,-1):
        prod = prod * nums[j+1]
        res[j]*=prod
    
    return res