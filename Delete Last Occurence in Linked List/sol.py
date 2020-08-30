def solve(self, node, target):
    if not node: return node
    
    p1 = None
    p2 = node
    
    while p2 and p2.next:
        if p2.next == target:
            p1 = p2
        p2 = p2.next
        
    if p1 == None:
        if p2.val == target or node.val == target:
            return node.next
        else:
            return node
            
    p1.next = p1.next.next
    
    return node