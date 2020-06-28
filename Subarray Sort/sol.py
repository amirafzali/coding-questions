def subarraySort(array):
    i, j = 0, len(array)-1
	
    for i in range(len(array)):
		if i==j: return [-1,-1]
		elif array[i] > array[i+1]: break
			
    for j in reversed(range(len(array))):
		if i==j: return [-1,-1]
		elif array[j] < array[j-1]: break

    smallest = min(array[i:j+1])
    largest = max(array[i:j+1])
	
    print(smallest, largest)
	
    while i >= 0 and smallest < array[i]: i-=1;
    while j < len(array) and largest > array[j]: j+=1;

    return [i+1,j-1]