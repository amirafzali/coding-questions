def binaryTreePaths(self, root):
    paths = []
    
    def search(node, path):
        if not node: return
        
        path.append(str(node.val))
        if not node.left and not node.right:
            paths.append(path[:])
            path.pop()
            return
        
        if node.left: search(node.left, path)
        if node.right: search(node.right, path)
            
        path.pop()
    
    search(root,[])
    return ["->".join(x) for x in paths]