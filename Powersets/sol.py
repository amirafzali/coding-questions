def powerset(array):
    res = [[]]
	
    for num in array:
		for i in range(len(res)):
			res.append(res[i] + [num])
	
    return res
