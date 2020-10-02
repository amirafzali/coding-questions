def treeToDoublyList(self, root):
    head = p = Node(0)
    if not root: return None
    
    stack = []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        save = current.right
        p.right = current
        p.right.left = p
        p.right.right = None
        p = p.right
        current = save
        
    p.right = head.right
    head.right.left = p

    return head.right