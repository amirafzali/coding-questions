def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        heap = []
        heapq.heapify(heap)
        
        for interval in intervals:
            if not heap or heap[0] > interval[0]:
                heapq.heappush(heap, interval[1])
            else:
                heapq.heappushpop(heap, interval[1])
                
        return len(heap)