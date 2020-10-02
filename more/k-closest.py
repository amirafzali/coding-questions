def findClosestElements(self, arr, k, x):
    closest = -1
    
    low, high = 0, len(arr)-1
    
    while low <= high:
        mid = low + (high-low)//2
        
        if arr[mid] == x:
            closest = mid
            break
        if closest == -1 or abs(arr[closest]-x) > abs(arr[mid]-x):
            closest = mid
        
        if x > arr[mid]: low = mid+1
        else: high = mid-1
    
    res = deque()
    p1, p2 = closest, closest+1
    
    while len(res) < k:
        if p1 >= 0 and p2 < len(arr):
            diff1 = abs(arr[p1]-x)
            diff2 = abs(arr[p2]-x)
            
            if diff1<diff2:
                res.appendleft(arr[p1])
                p1-=1
            elif diff1>diff2:
                res.append(arr[p2])
                p2+=1
            else:
                if arr[p1] < arr[p2]:
                    res.appendleft(arr[p1])
                    p1-=1
                else:
                    res.append(arr[p2])
                    p2+=1
        elif p1 >= 0:
            res.appendleft(arr[p1])
            p1-=1
        else:
            res.append(arr[p2])
            p2+=1
    
    return res