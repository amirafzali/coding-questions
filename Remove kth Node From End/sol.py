class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    p1 = p2 = head
	
    if not head: return None
	
    for i in range(k):
		if not p2: return head
		p2 = p2.next
	
    if not p2: 
		head.value = head.next.value
		head.next = head.next.next
		return head
	
    while(p2.next):
		p1 = p1.next
		p2 = p2.next

    if p1.next:
		p1.next = p1.next.next
    else:
		p1.next = None
	
    return head