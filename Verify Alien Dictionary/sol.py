def isAlienSorted(self, words, order):
    positions = {char:i for i,char in enumerate(order)}

    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        
        p = 0
        
        while p < len(word1) and p < len(word2):
            if positions[word1[p]] < positions[word2[p]]:
                break
            elif positions[word1[p]] > positions[word2[p]]: 
                return False
            p+=1
        
        if p < len(word1) and p >= len(word2): return False
            
    return True