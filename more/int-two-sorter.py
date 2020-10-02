def get(arr1,arr2):
    if not arr1 or not arr2: return []

    p1 = p2 = 0

    res = []
    while p1 < len(arr1) and p2 < len(arr2):
        n1, n2 = arr1[p1], arr2[p2]
        if n1 > n2:
            p2+=1
        elif n1 < n2:
            p1+=1
        else:
            res.append(n1)
            p1+=1
            p2+=1

    return res

print(get([1,1,1,2,3,4,4,5,5],[1,1,2,4,5,5]))