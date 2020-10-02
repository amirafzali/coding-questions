def read(self, buf, n):
    total = 0
    x = ['','','','']
    while True:
        r = read4(x)
        to_read = min(r,n-total)
        for i in range(to_read):
            buf[total+i] = x[i] 
        total+=to_read
        if total == n or r < 4: break
            
    return total