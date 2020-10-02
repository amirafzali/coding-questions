def nextPermutation(self, nums):
    
    if len(nums) == 1: return nums[0]
    
    def reverse(arr,start,end):
        for i in range(start,(start+end)//2+1):
            s = end+start-i
            arr[i],arr[s] = arr[s],arr[i]
            
    
    mark = -1
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            mark = i
            break
            
    if mark == -1:
        reverse(nums,0,len(nums)-1)
        return nums
            
    for i in range(len(nums)-1,mark,-1):
        if nums[i] > nums[mark]:
            nums[i],nums[mark] = nums[mark],nums[i]
            break
    
    reverse(nums,mark+1,len(nums)-1)
    return nums