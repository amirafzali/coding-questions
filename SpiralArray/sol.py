def spiralTraverse(array):
    res = []
	
    sC, eC, sR, eR = 0, len(array[0])-1, 0, len(array)-1
	
    while sC <= eC and sR <= eR:
		
		for i in range(sC, eC+1):
			res.append(array[sR][i])
		
		for i in range(sR+1, eR+1):
			res.append(array[i][eC])
		
		for i in range(eC-1, sC-1, -1):
			if sR==eR: break
			res.append(array[eR][i])
		
		for i in range(eR-1, sR, -1):
			if sC==eC: break
			res.append(array[i][sC])
		
		sC+=1
		eC-=1
		sR+=1
		eR-=1
	
    return res