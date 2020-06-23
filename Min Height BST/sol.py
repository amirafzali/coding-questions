def minHeightBst(array):
    mid = len(array)//2
    root = BST(array[mid])
    formTree(array, 0, mid-1, root)
    formTree(array, mid+1, len(array)-1, root)
    return root

def formTree(array, i, j, root):
	if i > j or not root: return
	mid = i+(j-i)//2
	root.insert(array[mid])
	formTree(array, i, mid-1, root)
	formTree(array, mid+1, j, root)