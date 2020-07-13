class MyQueue(object):

    def __init__(self):
        self.a = []
        self.b = []
        

    def push(self, x):
        self.a.append(x)
        

    def pop(self):
        if not self.a and not self.b: return None
        if not self.b: self.move()
        
        return self.b.pop()
        

    def peek(self):
        if not self.b: self.move()
        return self.b[-1]
        

    def empty(self):
        return len(self.a)+len(self.b) == 0
        
    def move(self):
        while self.a:
            self.b.append(self.a.pop())