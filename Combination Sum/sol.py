def combinationSum(self, candidates, target):  
    res = []
    candidates.sort()
    
    def explore(current, target, pos):
        if target == 0:
            res.append(current[:])
            return
        
        for i in range(pos, len(candidates)):
            if target >= candidates[i]:
                current.append(candidates[i])
                explore(current, target-candidates[i], i)
                current.pop()
            else:
                break
                
    explore([], target, 0)
    return res