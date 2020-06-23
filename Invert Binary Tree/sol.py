def invertBinaryTree(tree):
    if not tree: return
	
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    back = tree.left
    tree.left = tree.right
    tree.right = back
    return tree