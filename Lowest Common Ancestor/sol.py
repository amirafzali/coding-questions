def lowestCommonAncestor(self, root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    
    if left and right: return root
    if left: return left
    return right

def lowestCommonAncestor(self, root, p, q):
    parents = {root: None}
    
    stack = [root]
    
    while stack:
        current = stack.pop()
        if current.left:
            parents[current.left] = current
            stack.append(current.left)
        if current.right:
            parents[current.right] = current
            stack.append(current.right)
            
    p_parents = set([p])
    while p in parents:
        p = parents[p]
        p_parents.add(p)
    
    while q not in p_parents:
        q = parents[q]
    
    return q