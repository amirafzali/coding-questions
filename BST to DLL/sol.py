def treeToDoublyList(self, root):
    head = p = Node()
    current = root
    stack = []
    
    if not root: return root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
            
        current = stack.pop()
        p.right = current
        current.left = p
        p = current
        current = current.right
    
    p.right = head.right
    head.right.left = p
    return head.right