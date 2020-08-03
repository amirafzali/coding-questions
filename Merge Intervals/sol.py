def merge(self, intervals):
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    
    for i in range(1,len(intervals)):
        lastStart, lastEnd = res[-1]
        nextStart, nextEnd = intervals[i]
        
        if nextStart > lastEnd:
            res.append(intervals[i])
        else:
            res[-1][1] = max(lastEnd, nextEnd)
    
    return res