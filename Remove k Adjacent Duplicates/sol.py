def removeDuplicates(self, s, k):
    stack = []
    
    for char in s:
        if not stack or stack[-1][0] != char:
            stack.append([char,1])
        else:
            last = stack.pop()
            last[1] = (last[1]+1)%k
            if last[1] != 0:
                stack.append(last)
                
    return "".join([pair[0]*pair[1] for pair in stack])