def reverseList(self, head):
    last=None
    
    while head:
        temp = head.next
        head.next = last
        last = head
        head = temp
        
    return last