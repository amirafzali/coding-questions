def flatten(self, root):
    last = TreeNode()
    
    stack = []
    current = root
    
    while current or stack:
        while current:
            last.right = current
            save = current.left
            stack.append(current.right)
            current.left = None
            current.right = None
            current = save
            last = last.right
            
        current = stack.pop()
        
    return last