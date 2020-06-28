def numberOfWaysToMakeChange(n, denoms):
	change = {num: 0 for num in range(n+1)}
	change[0] = 1
	for num in denoms:
		for i in range(n+1):
			if i >= num:
				change[i]+= change[i-num]
	return change[n]