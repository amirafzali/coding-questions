def wordBreak(self, s, wordDict):
    lookup = set(wordDict)
    mem = {}
    
    def isValid(s, words, mem):
        if not s: return True
        if s in mem: return s[mem]
        for i in range(1,len(s)+1):
            if s[:i] in words and isValid(s[i:], words, mem):
                mem[s] = True
                return True
        mem[s] = False
        return False
    
    return isValid(s, lookup, mem)