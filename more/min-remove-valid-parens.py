def minRemoveToMakeValid(self, s):
    stack = []
    for i,char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if len(stack) == 0 or s[stack[-1]] != "(":
                stack.append(i)
            else:
                stack.pop()
                
    if not stack: return s
    
    pos = 0
    res = []
    for i in range(len(s)):
        if pos < len(stack) and i == stack[pos]:
            pos+=1
        else:
            res.append(s[i])
            
    return "".join(res)