def sortByHeight(a):
    sorted_list = sorted(a)
    p1 = 0
    while p1 < len(sorted_list) and sorted_list[p1] == -1:
        p1+=1
            
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = sorted_list[p1]
            p1+=1
            
    return a