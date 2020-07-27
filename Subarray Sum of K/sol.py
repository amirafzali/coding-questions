def subarraySum(self, nums, k):
    sums = {}
    rolling = count = 0
    
    for num in nums:
        rolling+=num
        
        if rolling == k: 
            count+=1
        if rolling-k in sums: 
            count+=sums[rolling-k]
        
        sums[rolling] = sums.get(rolling,0)+1
    
    return count