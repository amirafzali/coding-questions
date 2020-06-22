def validateBst(tree, minVal=float('-inf'), maxVal = float('inf')):
	if not tree: return True
	if tree.value < minVal or tree.value >= maxVal: return False
	
	return validateBst(tree.left, minVal, tree.value) and validateBst(tree.right, tree.value, maxVal)