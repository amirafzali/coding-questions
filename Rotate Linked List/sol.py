def rotateRight(self, head, k):
    if not head or not head.next: return head
    
    length = 0
    current = head
    while current:
        current=current.next
        length+=1
        
    k = k%length
    if k==0: return head
    
    p1 = p2 = head
    
    for i in range(k):
        p2 = p2.next
        
    while p2.next:
        p1 = p1.next
        p2 = p2.next
        
    ref = p1.next
    
    p1.next = None
    p2.next = head
    
    return ref