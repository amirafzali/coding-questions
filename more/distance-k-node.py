def distanceK(self, root, target, K):
    def search(root, parent=None):
        if not root: return
        root.parent = parent
        search(root.left,root)
        search(root.right, root)
    search(root)
    
    queue = deque()
    res = []
    queue.append((target,0))
    seen = set([target])
    
    while queue:
        node,dist = queue.popleft()
        if dist == K:
            res.append(node.val)
        
        else:
            if node.left and node.left not in seen:
                queue.append((node.left,dist+1))
                seen.add(node.left)
            
            if node.right and node.right not in seen:
                queue.append((node.right,dist+1))
                seen.add(node.right)
            
            if node.parent and node.parent not in seen:
                queue.append((node.parent,dist+1))
                seen.add(node.parent)
            
    return res