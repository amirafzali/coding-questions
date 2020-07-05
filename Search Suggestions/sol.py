def suggestedProducts(self, products, searchWord):
    products.sort()
    head = current = TrieNode()
    res = []
    
    for word in products:
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode(char)
            current = current.children[char]
            if len(current.words) < 3: current.words.append(word)
        current = head
    
    done = False
    for char in searchWord:
        if char in current.children and not done:
            current = current.children[char]
            res.append(current.words)
        else:
            done = True
            res.append([])
                
    return res