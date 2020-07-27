def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    flip = -1
    i = longest = 0
    
    for j in range(len(nums)):
        if nums[j] == 0:
                i = flip+1
                flip = j
        longest = max(longest, j-i+1)
    
    return longest