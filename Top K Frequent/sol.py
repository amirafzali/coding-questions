def topKFrequent(self, words, k):
    freq = Counter(words)
    maxheap = []
    
    heapq.heapify(maxheap)
    
    for d,v in freq.items(): heapq.heappush(maxheap, (-v,d))
        
    return [heapq.heappop(maxheap)[1] for i in range(k)]