def areSimilar(a, b):
    misplaced = []
    
    for i in range(len(a)):
        if a[i] != b[i]:
            if len(misplaced) == 2: return False
            misplaced.append(i)
    
    if len(misplaced) == 1: return False
    if len(misplaced) == 0: return True
    
    x,y = misplaced
    return a[x] == b[y] and a[y] == b[x]