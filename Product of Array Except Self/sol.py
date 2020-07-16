def productExceptSelf(self, nums):
    left = [1 for i in range(len(nums))]
    
    for i in range(1,len(left)):
        left[i] = nums[i-1]*left[i-1]
        
    current=1
    
    for j in range(len(left)-2, -1, -1):
        left[j] = current*nums[j+1]*left[j]
        current = current*nums[j+1]
    
    return left