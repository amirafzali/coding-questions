def mostCommonWord(self, paragraph, banned):
    bans = set(word.lower() for word in banned)
    paragraph = paragraph.lower()
    
    hits = re.findall(r"\w+",paragraph)
    freq = Counter(hits)
    print(freq)
    mostHits = 0
    word = ""
    
    for k,v in freq.items(): 
        if v > mostHits and k not in bans:
            mostHits = v
            word = k
            
    return word