def levenshteinDistance(str1, str2):
    mem = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    for i in range(len(str1)+1): mem[0][i] = i
    for i in range(len(str2)+1): mem[i][0] = i
	
    for i in range(1,len(mem)):
		for j in range(1,len(mem[0])):
			if str1[j-1] == str2[i-1]:
				mem[i][j] = mem[i-1][j-1]
			else:
				mem[i][j] = 1+min(mem[i-1][j], mem[i][j-1],mem[i-1][j-1])
    return mem[-1][-1]