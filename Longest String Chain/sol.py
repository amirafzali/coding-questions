def longestStrChain(self, words):
    wordset = set(words)
    longest = 0
    lookup = {}
    for word in words:
        longest = max(longest, self.search(wordset,word,lookup))
    return longest
    
def search(self, words, word, lookup):
    if not word or word not in words: return 0
    if word in lookup: return lookup[word]
    
    longest = 0
    for i in range(len(word)):
        longest = max(self.search(words, word[0:i]+word[i+1:], lookup)+1, longest)
    
    lookup[word] = longest
    
    return longest