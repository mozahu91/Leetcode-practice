class queue(object):
    
    def __init__(self):
        self.instack = []
        self.outstack = []
    
    def enqueue(self, item):
        self.instack.append(item)
    
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        
        return self.outstack.pop()
