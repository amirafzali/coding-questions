def reorderList(self, head):
    if not head or not head.next: return head
    
    p1 = p2 = head
    
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        
    last = None
    while p1:
        back = p1.next
        p1.next = last
        last = p1
        p1 = back
    
    p1, p2 = head, last

    while p2.next:
        back = p1.next
        p1.next = p2
        p1 = back
        
        back = p2.next
        p2.next = p1
        p2 = back
        
    return p1