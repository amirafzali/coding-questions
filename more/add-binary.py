def addBinary(self, a, b):
    p1 = len(a)-1
    p2 = len(b)-1
    
    carry = 0
    res = []
    while p1 >= 0 or p2 >= 0:
        current = carry
        carry = 0
        
        if p1>=0:
            current+=ord(a[p1])-48
            p1-=1
            
        if p2>=0:
            current+=ord(b[p2])-48
            p2-=1
            
        if current >= 2:
            carry = 1
        current = current%2
        res.append(chr(current+48))
        
    if carry: res.append('1')
    res.reverse()
    return ''.join(res)

def addBinary(self, a, b):
    n1, n2 = int(a,2), int(b,2)
    
    while n2:
        total = n1^n2
        carry = (n1&n2) << 1
        n1,n2 = total, carry
    
    return bin(n1)[2:]