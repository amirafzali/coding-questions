def maxSubArrayLen(self, nums, k):
    longest = 0
    rolling = 0
    prefix = {}
    for i,num in enumerate(nums):
        rolling+=num
        prefix[rolling] = prefix.get(rolling,i)
        
    rolling = 0
    for i in range(len(nums)):
        rolling+=nums[i]
        if rolling == k:
            longest = max(longest, i+1)
        else:
            target = rolling-k
            if target in prefix:
                longest = max(longest, i-prefix[target])
                
    return longest