# Two Stack Implementation
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
'''

# One Stack, Tuple Implementation
'''
class MinStack:
    def __init__(self):
        self.stack = []
    
    def push(self,val):
        if self.stack:
            curMin = min(val, self.getMin())
            self.stack.append((val, curMin))
        else:
            self.stack.append((val, val))
            
    def pop(self):
        self.stack.pop()
        
    def top(self):
        return self.stack[-1][0]
    
    def getMin(self):
        return self.stack[-1][1]
'''
