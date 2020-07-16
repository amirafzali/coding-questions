def plusOne(self, digits):
    carry = 1
    
    for i in range(len(digits)-1, -1, -1):
        total = carry+digits[i]
        carry = 0
        if total >= 10: 
            carry=1
            total%=10
        digits[i] = total
        
    if carry: digits = [1]+digits
    return digits