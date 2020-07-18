def isSymmetric(self, root):
    if not root: return True
    
    def check(left, right):
        if not left and not right: return True
        if not left or not right: return False
        
        c1 = check(left.left, right.right)
        c2 = check(left.right, right.left)
        
        return left.val == right.val and c1 and c2
    
    return check(root.left, root.right)