class Node:
    
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.size = 0
        
        self.head = Node()
        self.tail = Node()
        
        self.lookup = {}
        
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        if key not in self.lookup: return -1
        self.moveToFront(key)
        return self.lookup[key].value
    
    def moveToFront(self, key):
        if key not in self.lookup: return
        
        current = self.lookup[key]
        current.prev.next = current.next
        current.next.prev = current.prev
        
        store = self.head.next
        self.head.next = current
        current.prev = self.head
        
        current.next = store
        store.prev = current
        
    def addToFront(self, key, value):
        current = Node(key, value)
        self.lookup[key] = current
        
        store = self.head.next
        self.head.next = current
        current.prev = self.head
        
        current.next = store
        store.prev = current
        
        
    def removeLast(self):
        
        del self.lookup[self.tail.prev.key]
        
        ref = self.tail.prev.prev
        ref.next = self.tail
        self.tail.prev = ref
        
        

    def put(self, key, value):
        if key in self.lookup:
            self.lookup[key].value = value
            self.moveToFront(key)
            return
        
        if self.size == self.cap:
            self.removeLast()
        else:
            self.size+=1
        
        self.addToFront(key,value)