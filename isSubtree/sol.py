def isSubtree(self, s, t):
    def equal(s,t):
        if not s and not t: return True
        if not s or not t: return False
        
        return s.val == t.val and equal(s.left, t.left) and equal(s.right, t.right)
    
    return s and (equal(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right,t))