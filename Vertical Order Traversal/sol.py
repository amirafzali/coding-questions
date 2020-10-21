def verticalOrder(self, root):
    if not root: return []
    cols = defaultdict(list)
    queue = deque([(root,0)])
    smallest = largest = 0
    
    while queue:
        current, pos = queue.popleft()
        cols[pos].append(current.val)
        if current.left:
            queue.append((current.left,pos-1))
        if current.right:
            queue.append((current.right,pos+1))
        smallest = min(smallest,pos)
        largest = max(largest,pos)
        
    return [cols[i] for i in range(smallest,largest+1) if i in cols]