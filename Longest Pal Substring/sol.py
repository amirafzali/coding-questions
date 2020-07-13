def longestPalindrome(self, s):
	if len(s) <= 1: return s
	boundI, boundJ = 0, 1
	
	for i in range(1,len(s)):
		pal1 = self.getLongest(s, i-1, i)
		pal2 = self.getLongest(s, i, i)		
		comp1 = pal1[1]-pal1[0]
		comp2 = pal2[1]-pal2[0]
		if comp1 > boundJ-boundI: boundI, boundJ = pal1
		if comp2 > boundJ-boundI: boundI, boundJ = pal2
	
	return s[boundI:boundJ]

def getLongest(self, s, i, j):
	while i >= 0 and j < len(s):
		if s[i]!=s[j]: break
		i-=1
		j+=1
	
	return [i+1, j]