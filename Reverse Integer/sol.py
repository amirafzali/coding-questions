def reverse(self, x):
    count = 0
    neg = True if x<0 else False
    x = abs(x)
    
    while x > 0:
        count*=10
        count += x%10
        x = x//10
        
    if neg: count=-count
    # Overflow / Underflow Check
    if -2**31 <= count < 2**31: count = 0
    return count