def cloneGraph(self, node):
    if not node: return node
    graph = {}
    queue = deque([node])
    graph[node] = Node(node.val)
    
    
    while queue:
        current = queue.popleft()
        
        for n in current.neighbors:
            if n not in graph:
                graph[n] = Node(n.val)
                queue.append(n)
            
            graph[current].neighbors.append(graph[n])
                
    return graph[node]