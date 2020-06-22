def isMonotonic(array):
    desc = asc = True
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            asc = False
        if array[i] < array[i+1]:
			desc = False
			
    return asc or desc
