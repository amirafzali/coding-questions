def verticalOrder(self, root):
    if not root: return []
    small = large = 0
    
    queue = deque([(root,0)])
    res = defaultdict(list)
    
    while queue:
        for i in range(len(queue)):
            current = queue.popleft()
            res[current[1]].append(current[0].val)
            
            if current[0].left:
                small = min(small, current[1]-1)
                queue.append((current[0].left,current[1]-1))
                
            if current[0].right:
                large = max(large, current[1]+1)
                queue.append((current[0].right,current[1]+1))
                
    return [res[i] for i in range(small,large+1)]