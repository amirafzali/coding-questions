def isPalindrome(self, s):
    p1, p2 = 0, len(s)-1
    
    while p1 < p2:
        if not s[p1].isalnum():
            p1+=1
        elif not s[p2].isalnum():
            p2-=1
            
        else:
            if s[p1].lower() != s[p2].lower():
                return False
            p1+=1
            p2-=1
    
    return True