def inorderTraversal(self, root):
    stack = []
    res = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
            
        current = stack.pop()
        res.append(current.val)
        current = current.right
        
    return res