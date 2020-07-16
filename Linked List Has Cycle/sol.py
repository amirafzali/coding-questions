def hasCycle(self, head):
    p1 = p2 = head

    while p1 and p2:
        for i in range(2):
            p2 = p2.next
            if not p2: return False
        
        if p1 == p2: return True
            
        p1 = p1.next
        
    return False