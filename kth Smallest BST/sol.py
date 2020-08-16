def kthSmallest(self, root, k):
    def getkth(root, res):
        if not root: return
        
        getkth(root.left, res)
        res.append(root.val)
        getkth(root.right, res)
        
    res = []
    getkth(root,res)
    
    return res[k-1]