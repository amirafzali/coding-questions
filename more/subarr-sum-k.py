def subarraySum(self, nums, k):
    total = count = 0
    lookup = defaultdict(int)
    lookup[0]+=1
    
    for i in range(len(nums)):
        total+=nums[i]
        if total-k in lookup:
            count+=lookup[total-k]
            
        lookup[total]+=1
        
    return count