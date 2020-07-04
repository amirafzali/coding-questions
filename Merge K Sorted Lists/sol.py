def mergeKLists(self, lists):
    head = p1 = ListNode()
    heap = []
    heapq.heapify(heap)
    
    for p in lists: 
        if p: heapq.heappush(heap, (p.val, p))
        
    while heap:
        current = heapq.heappop(heap)[1]
        p1.next = current
        if current.next:
            current = current.next
            heapq.heappush(heap, (current.val, current))
        p1 = p1.next

    p1.next = None
    
    return head.next