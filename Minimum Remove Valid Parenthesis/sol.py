def minRemoveToMakeValid(self, s):
    stack = []
    
    for i in range(len(s)):
        if s[i] == ")" and stack and s[stack[-1]] == "(":
            stack.pop()
        elif s[i] == "(" or s[i] == ")":
            stack.append(i)
    
    lookup = set(stack)
    
    return "".join([s[i] for i in range(len(s)) if i not in lookup])