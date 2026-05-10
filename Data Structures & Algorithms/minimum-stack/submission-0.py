class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # keeping track of min value at each point

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val_at_point = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val_at_point)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
