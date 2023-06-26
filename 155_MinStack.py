class MinStack:

    def __init__(self):
        self.stack = []
        self.min_vals = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_vals.append(val if not self.min_vals else min(val, self.min_vals[-1]))
        

    def pop(self) -> None:
        self.min_vals.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_vals[-1]