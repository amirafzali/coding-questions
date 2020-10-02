def reorderList(self, head):
    if not head or not head.next or not head.next.next:
        return head
    
    p1 = p2 = head
    
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
    
    if p2: p1 = p1.next
    
    last = None
    while p1:
        save = p1.next
        p1.next = last
        last = p1
        p1 = save

    p1 = head
    p2 = last

    while p2:
        save = p1.next
        p1.next = p2
        p1 = save
        
        save = p2.next
        p2.next = p1
        p2 = save
    
    p1.next = None
    
    return head