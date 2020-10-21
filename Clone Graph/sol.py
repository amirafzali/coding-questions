def cloneGraph(self, node):
    if not node: return node
    cloned = {node: Node(node.val)}
    queue = deque([node])
    
    while queue:
        current = queue.popleft()
        for n in current.neighbors:
            n_node = None
            if n in cloned:
                n_node = cloned[n]
            else:
                n_node = Node(n.val)
                cloned[n] = n_node
                queue.append(n)
                
            cloned[current].neighbors.append(n_node)
    
    return cloned[node]