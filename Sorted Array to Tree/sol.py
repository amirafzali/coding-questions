def sortedArrayToBST(self, nums):
    if not nums: return None

    def fillTree(i, j, nums):
        if i > j: return None
        mid = i + (j-i)//2
        root = TreeNode(nums[mid])
        root.left = fillTree(i, mid-1, nums)
        root.right = fillTree(mid+1, j, nums)
        
        return root

    return fillTree(0, len(nums)-1, nums)