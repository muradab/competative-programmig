class MinStack:

    def __init__(self):
        self.stack = []
        self.minNum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
       
        if len(self.stack) == 1:
            self.minNum.append(val)
        else : 
            if self.minNum[-1] > val:
                self.minNum.append(val)
                
        
    def pop(self) -> None:
        if (len(self.stack) == 0):
            return
        else :
            self.stack.pop()
            if self.minNum[-1] not in self.stack:
                self.minNum.pop()

    def top(self) -> int:
        if len(self.stack) <= 0:
           
            return 
        else :
            return self.stack[-1]
        

    def getMin(self) -> int:
      
        return self.minNum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()