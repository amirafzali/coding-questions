def canAttendMeetings(self, intervals):
    if len(intervals) <= 1: return True
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1,len(intervals)):
        lastS,lastE = intervals[i-1]
        nextS,nextE = intervals[i]
        
        if nextS < lastE: return False
        
    return True