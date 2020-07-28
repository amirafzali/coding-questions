# Bottom up
def lengthOfLIS(self, nums):
    if len(nums) <= 1: return len(nums)
    paths = [1 for num in nums]
    
    for i in range(len(nums)-2, -1, -1):
        longest = paths[i]
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                longest = max(longest, 1+paths[j])
        paths[i] = longest
        
    return max(paths)


# Top down
def lengthOfLIS(self, nums):
    if len(nums) <= 1: return len(nums)
    mem = {}
    longest = 1
    
    def getLength(n):
        if n in mem: return mem[n]
        longest = 1
        
        for i in range(n+1, len(nums)):
            if nums[i] > nums[n]:
                longest = max(longest, getLength(i)+1)
        
        mem[n] = longest
        return mem[n]
    
    for i in range(len(nums)):
        longest = max(getLength(i), longest)
        
    return longest