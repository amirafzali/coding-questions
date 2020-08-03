def minMeetingRooms(self, intervals):
    if len(intervals) <= 1: return len(intervals)
    
    intervals.sort(key = lambda x: x[0])
    rooms = [intervals[0][1]]
    heapq.heapify(rooms)
    
    for i in range(1,len(intervals)):
        if intervals[i][0] >= rooms[0]:
            heapq.heappushpop(rooms, intervals[i][1])
        else:
            heapq.heappush(rooms,intervals[i][1])
            
    return len(rooms)