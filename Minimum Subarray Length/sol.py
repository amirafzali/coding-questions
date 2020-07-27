def minSubArrayLen(self, s, nums):
    i = j = count = 0
    smallest = len(nums)+1
    
    while i <= j and j < len(nums):
        if nums[j] >= s: return 1
        count += nums[j]
        if count >= s:
            smallest = min(smallest, j-i+1)
            count-=nums[i]+nums[j]
            i+=1
        else:
            j+=1
            
    return smallest if smallest <= len(nums) else 0