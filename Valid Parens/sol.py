def isValid(self, s):
    stack = []
    lookup = {'}':'{', ']':'[', ')':'('}
    
    for char in s:
        if char in lookup:
            if len(stack) == 0: return False
            if stack.pop() != lookup[char]: return False
        else: stack.append(char)
        
    return len(stack) == 0