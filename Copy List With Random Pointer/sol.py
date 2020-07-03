def copyRandomList(self, head):
    copyHead = current = Node(0)
    pointer = head
    links = {}
    
    
    while pointer:
        current.next = Node(pointer.val)
        current = current.next
        links[pointer] = current
        pointer = pointer.next
        
    pointer = head
    current = copyHead.next
    
    while pointer:
        if pointer.random: current.random = links[pointer.random]
        else: current.random = None
            
        pointer = pointer.next
        current = current.next
    
    return copyHead.next