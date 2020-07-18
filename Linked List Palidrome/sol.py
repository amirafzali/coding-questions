def isPalindrome(self, head):
    p1 = p2 = head
    
    if not head or not head.next: return True
    
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next

    p2 = p1
        
    last = None
    while p2:
        store = p2.next
        p2.next = last
        last = p2
        p2 = store
    
    p1, p2 = head, last
    
    while p2: 
        if p1.val != p2.val: return False
        p1 = p1.next
        p2 = p2.next
    
    return True