def isBipartite(self, graph):
    types = {}
    queue = deque()
    for i in range(len(graph)):
        if i not in types:
            queue.append(i)
            types[i] = 1
            
            while queue:
                current = queue.popleft()
                for n in graph[current]:
                    if n not in types:
                        queue.append(n)
                        types[n] = -types[current]
                    if types[n] == types[current]: return False
                    
    return True