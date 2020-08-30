def solve(self, root, k):
    if not root:
        return root
        
    if root.left and root.right:
        if root.left.val == k: return root.right.val
        elif root.right.val == k: return root.left.val
    
    leftSearch = self.solve(root.left, k)
    if leftSearch != None: return leftSearch
    return self.solve(root.right, k)