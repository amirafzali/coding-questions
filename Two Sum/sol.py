class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}
        for i,num in enumerate(nums):
            hit = target-num
            if hit in lookup: return [lookup[hit], i]
            lookup[num] = i
        
        return [-1,-1]