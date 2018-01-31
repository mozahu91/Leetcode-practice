# Single List implementation

class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        
    def _repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)
            
            
