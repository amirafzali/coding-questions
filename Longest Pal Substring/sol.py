def longestPalindromicSubstring(string):
	longest = string[0]
	for i in range(len(string)):
		try1 = palLength(string, i, i)
		try2 = palLength(string, i-1, i)
		word1 = string[try1[0]:try1[1]+1]
		word2 = string[try2[0]:try2[1]+1]
		if len(word1) > len(longest): longest = word1
		if len(word2) > len(longest): longest = word2
	
	return longest
	
def palLength(word, i, j):
	while i >= 0 and j < len(word):
		if word[i] != word[j]:
			break
		i-=1
		j+=1
	return [i+1, j-1]