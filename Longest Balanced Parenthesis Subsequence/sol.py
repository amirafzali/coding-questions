def solve(self, s):
    length = 0
    balanced = 0
    
    for char in s:
        if char == ")" and balanced < 0:
            balanced+=1
            length+=2
        elif char == "(":
            balanced-=1
            
    return length