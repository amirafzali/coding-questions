def findMin(self, nums):
    i, j = 0, len(nums)-1
    if nums[-1] > nums[0]: return nums[0]
    
    smallest = nums[0]
    start, end  = nums[0], nums[-1]
    
    while i <= j:
        mid = i+(j-i)//2
        
        smallest = min(smallest, nums[mid])
        
        if nums[mid] <= end:
            j=mid-1
        elif nums[mid] >= start:
            i=mid+1
        
    return smallest