class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.k = k
        
        

    def insertFront(self, value: int) -> bool:
        if self.isFull() :
            return False
        else :
            self.deque.insert(0,value)
            return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull() :
            return False
        else :
            self.deque.append(value)
            return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty() :
            return False
        else :
            self.deque.pop(0)
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty() :
            return False
        else :
            self.deque.pop()
            return True
        

    def getFront(self) -> int:
        if self.isEmpty() :
            return -1
        else :
            return self.deque[0]
        

    def getRear(self) -> int:
        if self.isEmpty() :
            return -1
        else :
            return self.deque[-1]
            
        
        

    def isEmpty(self) -> bool:
        if len(self.deque) == 0 :
            return True
        else :
            return False
        
        

    def isFull(self) -> bool:
        if len(self.deque) == self.k :
            return True
        else :
            return False
            
        


