def isValidBST(self, root):
	def isValid(root, most, least):
		if not root: return True
		left = isValid(root.left, root.val, least)
		right = isValid(root.right, most, root.val)

		return least < root.val < most and left and right
	
	return isValid(root, float('inf'), float('-inf'))

def isValidBST(self, root):
	if not root: return True
	stack = []
	current = root
	last = float('-inf')
	
	while stack or current:
		while current:
			stack.append(current)
			current = current.left

		current = stack.pop()
		if current.val <= last: return False
		last = current.val
		current = current.right
	
	return True