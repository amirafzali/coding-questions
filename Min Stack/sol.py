class Node:
    def __init__(self, val, m):
        self.val = val
        self.min = m

class MinStack(object):

    def __init__(self):
        self.stack = []
        
    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append(Node(x, x))
        else:
            self.stack.append(Node(x, min(self.getMin(), x)))
        

    def pop(self):
        if len(self.stack) > 0: self.stack.pop()
        

    def top(self):
        return self.stack[-1].val
        

    def getMin(self):
        return self.stack[-1].min