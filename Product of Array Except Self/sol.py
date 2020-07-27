def productExceptSelf(self, nums):
    left = [1 for i in range(len(nums))]
    
    for i in range(1,len(left)):
        left[i] = nums[i-1]*left[i-1]
        
    current=1
    
    for j in range(len(left)-2, -1, -1):
        left[j] = current*nums[j+1]*left[j]
        current = current*nums[j+1]
    
    return left


# With Division
def productExceptSelf(self, nums):
    if not nums or len(nums) <= 1: return nums
    zeroes = nums.count(0)
    prod = reduce(lambda tot,elm: tot*elm if elm!= 0 else tot, nums, 1)
    
    for i,num in enumerate(nums):
        if zeroes:
            if num == 0 and zeroes == 1:
                nums[i] = prod
            else:
                nums[i] = 0
        
        else:
            nums[i] = prod/num
    
    return nums