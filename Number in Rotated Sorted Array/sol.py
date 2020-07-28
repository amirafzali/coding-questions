# One pass


# Finding pivot
def search(self, nums, target):
    if not nums: return -1
    smallest = 0
    end = nums[-1]
    
    
    i, j = 0, len(nums)-1
    while i <= j:
        mid = i + (j-i)//2
        smallest = mid if nums[mid] < nums[smallest] else smallest
        if nums[mid] == target: return mid
        elif nums[mid] >= end: i+=1
        else: j-=1

    if smallest == 0:
        res = self.binary(0,len(nums)-1, nums, target)
        if res != -1: return res
    else:
        res1 = self.binary(0,smallest-1, nums, target)
        res2 = self.binary(smallest,len(nums)-1, nums, target)
        
        if res1 != -1: return res1
        elif res2 != -1: return res2
        
    return -1
        
def binary(self, i, j, nums, target):
    while i<=j:
        mid = i + (j-i)//2
        if nums[mid] == target: return mid
        elif nums[mid] < target: i = mid+1
        else: j = mid-1
            
    return -1