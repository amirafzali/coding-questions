class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeNthFromEnd(self, head, n):
    p1 = p2 = head
    if not head: return None
    
    for i in range(n): p2 = p2.next
    
    if not p2: return head.next
    
    while p2.next:
        p1 = p1.next
        p2 = p2.next
        
    p1.next = p1.next.next
    
    return head