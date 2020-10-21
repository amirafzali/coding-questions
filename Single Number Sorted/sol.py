def singleNonDuplicate(self, nums):
    low, high = 0, len(nums)-1
    
    while low <= high:
        mid = low + (high-low)//2
        if mid == 0 or mid == len(nums)-1:
            return nums[mid]
        if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
            return nums[mid]
        
        elif nums[mid] == nums[mid-1]:
            if mid%2==0:
                high = mid-2
            else:
                low = mid+1
        else:
            if mid%2==0:
                low = mid+2
            else: 
                high = mid-1
    
    return -1