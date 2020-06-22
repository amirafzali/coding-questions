def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	
	i = j = 0
	smallest = float('inf')
	res = []
	
	while i < len(arrayOne) and j < len(arrayTwo):
		num1 = arrayOne[i]
		num2 = arrayTwo[j]
		diff = abs(num1-num2)
		if diff < smallest:
			res = [num1,num2]
			smallest = diff
			
		if arrayOne[i] > arrayTwo[j]:
			j+=1
		else:
			i+=1
	
	return res