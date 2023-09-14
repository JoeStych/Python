class stack:
    def __init__(self):
        self.data = []
        self.count = 0
    
    def size(self):
        return self.count
    
    def empty(self):
        return self.count == 0
    
    def initialize(self):
        self.data = []
        count = 0
    
    def push(self, item):
        self.data.append(item)
        self.count += 1
        
    def pop(self):
        self.count -= 1
        x = self.data[self.count]
        del self.data[self.count]
        return x
    
    def print(self):
        for x in self.data:
            print(x)
            

class queue:
    def __init__(self):
        self.data = []
        self.back = 0
    
    def size(self):
        return self.back - self.front

    def print(self):
        for x in self.data in range(self.front, self.back):
            print(x)
            
    def enqueue(self, item):
        self.data.append(item)
        self.back += 1
        
    def dequeue(self):
        x = self.data[0]
        del self.data[0]
        self.back -= 1
        return x
    
    def make_empty(self):
        self.data = []
        self.back = 0
    
    def empty(self):
        return self.front == self.back
    