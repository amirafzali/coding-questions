def removeDuplicates(self, nums):
    if not nums: return 0
    
    length = 0
    
    for i in range(1,len(nums)):
        if nums[i] != nums[length]:
            length+=1
            nums[i],nums[length] = nums[length], nums[i]
    
    return length+1