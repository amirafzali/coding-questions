def longestValidParentheses(self, s):
    opened = closed = longest = 0
    for char in s:
        if char == '(':
            opened+=1
        else:
            closed+=1
        
        if opened==closed:
            longest = max(longest,opened*2)
        elif closed > opened:
            opened = closed = 0
    
    opened = closed = 0
    for char in s[::-1]:
        if char == '(':
            opened+=1
        else:
            closed+=1
        
        if opened==closed:
            longest = max(longest,opened*2)
        elif opened > closed:
            opened = closed = 0
    
    return longest