def diameterOfBinaryTree(self, root):
    if not root: return 0
    def findWidth(root):
        if not root:
            return (0,0)

        resLeft = findWidth(root.left)
        resRight = findWidth(root.right)
        
        path = max(resLeft[1]+resRight[1]+1,resLeft[0],resRight[0])
        depth = max(resLeft[1],resRight[1])+1
        
        return (path, depth)
    
    return max(findWidth(root))-1