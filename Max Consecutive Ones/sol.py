def findMaxConsecutiveOnes(self, nums):
    count = 0
    longest = 0
    
    for num in nums:
        count = count + 1 if num == 1 else 0
        longest = max(count, longest)
        
    return longest