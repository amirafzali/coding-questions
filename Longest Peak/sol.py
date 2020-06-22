def longestPeak(array):
	if len(array) <= 2: return 0
	
	start = longest = 0
	peaked = False
	
	for i in range(1, len(array)):
		print(i,array[i], peaked, start, longest)
		
		if array[i-1] == array[i]:
			start = i
			peaked = False
		elif array[i-1] > array[i] and not peaked:
			if start == i-1:
				start = i
			else: peaked = True
		elif array[i-1] < array[i] and peaked:
			peaked = False
			start = i-1
			
		if peaked: longest = max(longest, i-start+1)
			
	return longest