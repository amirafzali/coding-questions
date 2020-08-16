def findKthLargest(self, nums, k):
    heap = []
    heapq.heapify(heap)
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap,num)
        else:
            heapq.heappushpop(heap,num)

    return heapq.heappop(heap)