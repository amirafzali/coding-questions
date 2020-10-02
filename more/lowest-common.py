def lowestCommonAncestor(self, root, p, q):
    def search(root):
        if root == p or root == q or not root:
            return root

        left = search(root.left)
        right = search(root.right)

        if left == p and right == q or left == q and right == p:
            return root

        if left: return left

        else: return right
        
    return search(root)