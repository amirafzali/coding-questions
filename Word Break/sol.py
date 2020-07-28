def wordBreak(s, wordDict):
    states = set()
    words = set(word for word in wordDict)
    
    return self.search(s, words, 0, states)
    
def search(s, words, pos, states):
    if pos >= len(s): return True
    
    for i in range(pos, len(s)):
        if s[pos:i+1] in words and i+1 not in states and self.search(s, words, i+1, states):
            return True
        
    states.add(pos)
    return False


# Alt
def wordBreak(self, s, wordDict):
    lookup = set(wordDict)
    mem = set()
    
    def search(pos):
        if pos in mem: return False
        if pos >= len(s): return True
        
        for i in range(pos, len(s)):
            if s[pos:i+1] in lookup and search(i+1):
                return True
        
        mem.add(pos)
        return False
    
    return search(0)