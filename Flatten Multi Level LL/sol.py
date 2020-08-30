def flatten(self, head):
    if not head: return head
    current = head
    last = Node()
    stack = []
    
    while current or stack:
        while current:
            if current.next: stack.append(current.next)
            last.next = current
            last.child = None
            back = last
            last = last.next
            last.prev = back
            current = current.child
            
        if stack: current = stack.pop()
    head.prev = None
    
    return head