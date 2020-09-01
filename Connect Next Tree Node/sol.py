def connect(self, root):
    if not root: return root
    queue = deque([root])
    
    while queue:
        size = len(queue)
        for i in range(size):
            current = queue.popleft()
            if i < size-1:
                current.next = queue[0]
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
            
    return root