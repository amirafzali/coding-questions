def rotate(self, nums, k):
    n=k%len(nums)
    if n == 0: return nums
    
    for i in range(len(nums)//2):
        nums[i],nums[len(nums)-i-1] = nums[len(nums)-i-1],nums[i]
        
    for i in range(n//2):
        nums[i],nums[n-i-1] = nums[n-i-1],nums[i]
        
    for i in range(n, n+(len(nums)-n)//2):
        nums[i],nums[len(nums)-i+n-1] = nums[len(nums)-i+n-1],nums[i]
        
    return nums