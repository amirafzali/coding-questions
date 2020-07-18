def isValidBST(self, root):
	def isValid(root, most, least):
		if not root: return True
		left = isValid(root.left, root.val, least)
		right = isValid(root.right, most, root.val)

		return least < root.val < most and left and right
	
	return isValid(root, float('inf'), float('-inf'))