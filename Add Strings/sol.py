def addStrings(self, num1, num2):
    p1, p2 = len(num1)-1, len(num2)-1
    carry = 0
    res = []
    
    while p1 >= 0 or p2 >= 0 or carry:
        total = carry
        carry = 0
        if p1 >= 0:
            total += ord(num1[p1])-48
            p1-=1
            
        if p2 >= 0:
            total+=ord(num2[p2])-48
            p2-=1
        
        if total >= 10:
            total%=10
            carry = 1
            
        res.append(chr(total+48))
        
    return "".join(res[::-1])