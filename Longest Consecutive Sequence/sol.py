def longestConsecutive(self, nums):
    if len(nums) <= 1: return len(nums)
    valid = set(nums)
    longest = 1
    
    for val in valid:
        if val-1 not in valid:
            current = 0
            num = val
            while num in valid:
                num+=1
                current+=1
            longest = max(longest, current)
        
    return longest