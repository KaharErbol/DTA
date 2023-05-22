class Queue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        self.stack_in.append(x)
        
    def pop(self):
        if len(self.stack_out) == 0:
            self.transfer()
        return self.stack_out.pop()
        

    def peek(self):
        if len(self.stack_out) == 0:
            self.transfer()
        return self.stack_out[-1]
        
    
    def empty(self):
        return len(self.stack_in) == 0 and len(self.stack_out) == 0
        

    def transfer(self):
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())