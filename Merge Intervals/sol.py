def merge(self, intervals):
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    
    for i in range(1, len(intervals)):
        refstart, refend = res[-1]
        start, end = intervals[i]
        
        if start <= refend and end > refend:
            res[-1][1] = end
        elif start > refend:
            res.append(intervals[i])
            
    return res