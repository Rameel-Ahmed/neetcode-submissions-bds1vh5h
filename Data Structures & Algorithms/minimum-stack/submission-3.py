class MinStack:

    def __init__(self):

        self.list1=[]
        self.stack=[]

    def push(self, val: int) -> None:
        
        self.list1.append(val)
        self.stack.append(min(self.list1) if self.stack else val)

        

    def pop(self) -> None:
        self.list1.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.list1[-1]
        

    def getMin(self) -> int:
        return self.stack[-1]
        
