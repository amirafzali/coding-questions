def minRewards(scores):
	res = [1 for i in scores]
	
	for i in range(1, len(scores)):
		if scores[i] > scores[i-1]:
			res[i] = max(res[i],res[i-1]+1)
			
	for i in range(len(scores)-2, -1, -1):
		if scores[i] > scores[i+1]:
			res[i] = max(res[i],res[i+1]+1)
			
	return sum(res)