def merge(self, nums1, m, nums2, n):
    p1 = m-1
    p2 = n-1
    track = len(nums1)-1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[track] = nums2[p2]
            p2-=1
        else:
            nums1[track] = nums1[p1]
            p1-=1
        track-=1
        
    while p1 >= 0:
        nums1[track] = nums1[p1]
        p1-=1
        track-=1
        
    while p2 >= 0:
        nums1[track] = nums2[p2]
        p2-=1
        track-=1
        
    return nums1