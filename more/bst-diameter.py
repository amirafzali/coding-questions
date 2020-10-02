def diameterOfBinaryTree(self, root):
    
    def search(root):
        if not root: return [0,0]

        left = search(root.left)
        right = search(root.right)
        
        greatest_path = max(1+left[0], 1+right[0])
        greatest_overall = max(left[1],right[1],left[0]+right[0])
        return [greatest_path, greatest_overall]
    
    return search(root)[1]