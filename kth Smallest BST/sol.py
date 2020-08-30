def kthSmallest(self, root, k):
    def getkth(root, res):
        if not root: return
        
        getkth(root.left, res)
        res.append(root.val)
        getkth(root.right, res)
        
    res = []
    getkth(root,res)
    
    return res[k-1]

def solve(self, root, k):
    stack = []
    current = root
    smallest = -1
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
            
        current = stack.pop()
        smallest+=1
        if smallest == k: return current.val
        current = current.right