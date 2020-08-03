def eraseOverlapIntervals(self, intervals):
    if len(intervals) <= 1: return 0
    intervals.sort(key=lambda x: x[1])
    lastEnd = intervals[0][1]
    count = 0
    for i in range(1,len(intervals)):
        nextStart, nextEnd = intervals[i]
        if nextStart < lastEnd:
            count+=1
        else:
            lastEnd = nextEnd
    
    return count