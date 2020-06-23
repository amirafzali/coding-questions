def maxSubsetSumNoAdjacent(array):
	if not len(array): return 0
	for i in range(1,len(array)):
		if i == 1: array[i] = max(array[i],array[i-1])
		else: array[i] = max(array[i-1],array[i-2]+array[i])
	return array[-1]