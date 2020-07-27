def threeSumClosest(self, nums, target):
    closest = float('inf')
    nums.sort()
    
    for i in range(len(nums)-2):
        j, k = i+1, len(nums)-1
        
        while j < k:
            total = nums[i]+nums[j]+nums[k]
            if abs(total-target) < abs(closest-target): closest = total
            
            if total == target: return target
            elif total < target: j+=1
            else: k-=1
                
    return closest