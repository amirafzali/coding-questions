def ladderLength(self, beginWord, endWord, wordList):
    lookup = set(wordList)
    if endWord not in lookup: return 0
    count = 1
    queue = deque([beginWord])

    while queue:
        for i in range(len(queue)):
            current = queue.popleft()
            if current == endWord: return count
            for i in range(len(current)):
                for char in string.ascii_lowercase:
                    test = current[:i]+char+current[i+1:]
                    if test in lookup:
                        queue.append(test)
                        lookup.remove(test)
                        
        count+=1
        

    return 0