def mergeKLists(self, lists):
    if not lists: return None
    
    heap = []
    heapq.heapify(heap)
    head = track = ListNode()
    
    for p in lists:
        if p: heapq.heappush(heap, (p.val, p))
        
    while heap:
        current = heapq.heappop(heap)[1]
        track.next = current
        track = track.next
        current = current.next
        if current: heapq.heappush(heap, (current.val, current))
            
    return head.next