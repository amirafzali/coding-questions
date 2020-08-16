def maxPathSum(self, root):
    def getPaths(root):
        if not root: return [float('-inf'),float('-inf')]

        considerLeft = getPaths(root.left)
        considerRight = getPaths(root.right)
        
        maxPath = max(root.val+considerLeft[0],root.val+considerRight[0],root.val)
        maxPossible = max(maxPath,root.val+considerLeft[0]+considerRight[0],considerLeft[1],considerRight[1])
        
        return [maxPath,maxPossible]
    
    return max(getPaths(root))