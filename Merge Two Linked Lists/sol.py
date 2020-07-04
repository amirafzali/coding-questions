def mergeTwoLists(self, l1, l2):
    head = current = ListNode()
    
    p1, p2 = l1, l2
    
    while p1 and p2:
        if p1.val <= p2.val:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next

        current = current.next
    
    current.next = p1 if p1 else p2
    return head.next