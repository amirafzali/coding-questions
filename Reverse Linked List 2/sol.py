def reverseBetween(self, head, m, n):
    if m == n: return head
    
    count = 1
    current = connection = head
    while count != m:
        connection = current
        current = current.next
        count+=1
    
    last = None
    nextCon = current
    while count <= n:
        save = current.next
        current.next = last
        last = current
        current = save
        count+=1
        
    nextCon.next = current
    
    if m == 1:
        return last
    
    connection.next = last
    return head