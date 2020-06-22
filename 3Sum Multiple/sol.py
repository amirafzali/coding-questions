def threeNumberSum(array, targetSum):
	array.sort()
	results = []
	for i in range(len(array)-2):
		num = array[i]
		j = i+1
		k = len(array)-1
		while j < k:
			total = num+array[j]+array[k]
			if total == targetSum:
				results.append([num,array[j],array[k]])
				j+=1
				k-=1
			elif total > targetSum:
				k-=1
			else:
				j+=1
	
	return results