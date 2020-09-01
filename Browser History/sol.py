class BrowserHistory(object):
    def __init__(self, homepage):
        self.history = [homepage]
        self.pos = self.end = 0
        
    def visit(self, url):
        self.pos+=1
        if self.pos == len(self.history):
            self.history.append(url)
        else:
            self.history[self.pos] = url
        self.end = self.pos

    def back(self, steps):
        self.pos = max(0,self.pos-steps)
        return self.history[self.pos]
        
    def forward(self, steps):
        self.pos = min(self.end,self.pos+steps)
        return self.history[self.pos]