def permute(self, nums):
    res = []
    used = set()
    
    def search(current):
        if len(used) == len(nums):
            res.append(current[:])
            return
        
        for i in range(len(nums)):
            if i not in used:
                used.add(i)
                current.append(nums[i])
                search(current)
                used.remove(i)
                current.pop()
    
    search([])
    return res