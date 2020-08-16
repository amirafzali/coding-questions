def preorderTraversal(self, root):
    if not root: return []
    stack = []
    res = []
    current = root
    while current or stack:
        while current:
            res.append(current.val)
            stack.append(current)
            current = current.left
        current = stack.pop()
        current = current.right
            
    return res