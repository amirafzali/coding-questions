def maxProduct(self, nums):
    if not nums: return 1
    greatest = current_min = current_max = nums[0]
    
    for i in range(1,len(nums)):
        num = nums[i]
        back = max(num, current_max*num, current_min*num)
        current_min = min(num, current_max*num, current_min*num)
        current_max = back
        
        greatest = max(current_max, greatest)
        
    return greatest