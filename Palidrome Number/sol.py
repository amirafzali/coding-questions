def isPalindrome(self, x):
    if 0 <= x < 10: return True
    if x < 0 or x%10 == 0: return False

    
    count = 0
    
    while x > count:
        count*=10
        count+=x%10
        x//=10
        
        if x == count: return True
        
    return x==count or count//10 == x