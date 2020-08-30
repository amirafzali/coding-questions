def removeDuplicates(self, s, k):
    stack = []
    for char in s:
        if not stack:
            stack.append((char,1))
        else:
            count = 1
            if stack[-1][0] == char:
                count = stack[-1][1]+1
            
            if count == k:
                for i in range(k-1):
                    stack.pop()
            else:
                stack.append((char,count))
                
    return "".join([tup[0] for tup in stack])