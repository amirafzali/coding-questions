#O(n) O(1)
def addTwoNumbers(self, l1, l2):
    def reverse(l):
        last = None
        while l:
            save = l.next
            l.next = last
            last = l
            l = save
        return last
    
    l1 = reverse(l1)
    l2 = reverse(l2)
    
    carry = 0
    new_head = current = ListNode()
    
    while l1 or l2:
        total = carry
        carry = 0
        use = None
        
        if l1:
            total+=l1.val
            use = l1
            l1 = l1.next
        
        if l2:
            total+=l2.val
            use = l2
            l2 = l2.next
            
        if total >= 10: carry =1
        total%=10
        use.val = total
        current.next = use
        current = current.next
        
    if carry: current.next = ListNode(1)
    
    
    return reverse(new_head.next)

# O(n) O(n)
def addTwoNumbers(self, l1, l2):
    s1, s2 = [], []
    
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next
        
    new_head = current = ListNode()
    
    carry=0
    while s1 or s2:
        total = carry
        carry = 0
        
        if s1:
            total+=s1.pop()
        if s2:
            total+=s2.pop()
            
        if total >= 10: carry=1
        total%=10
        
        current.next = ListNode(total)
        current = current.next
        
    if carry: current.next = ListNode(1)

    last = None
    current = new_head.next
    while current:
        save = current.next
        current.next = last
        last = current
        current = save
        
    return last