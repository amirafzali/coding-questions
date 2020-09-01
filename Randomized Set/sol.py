class RandomizedSet(object):
    def __init__(self):
        self.arr = []
        self.lookup = {}
        

    def insert(self, val):
        if val in self.lookup: return False
        self.arr.append(val)
        self.lookup[val] = len(self.arr)-1
        return True

    def remove(self, val):
        if val not in self.lookup: return False
        
        if self.lookup[val] != len(self.arr)-1:
            pos = self.lookup[val]
            self.arr[pos],self.arr[-1] = self.arr[-1],self.arr[pos]
            if len(self.arr) > 1: self.lookup[self.arr[pos]] = pos
        
        del self.lookup[val]
        self.arr.pop()
        
        return True
        

    def getRandom(self):
        return self.arr[int(math.floor(len(self.arr)*random.random()))]