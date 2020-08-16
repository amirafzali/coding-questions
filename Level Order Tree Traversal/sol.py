def levelOrder(self, root):
    if not root: return []
    queue = deque()
    res = []
    queue.append(root)
    
    while queue:
        res.append([])
        for i in range(len(queue)):
            node = queue.popleft()
            res[-1].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    return res