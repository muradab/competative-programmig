class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None 

class Solution :
    def swapNodes (self,head):
        count = 1 
        current = head

        while current :
            if count == 1 :
                print("odd arrival")
                prev = current
                count += 1
                print(current.val)
                current = current.next
            else :
                print("from swap")
                print(current.val)
                temp = current
                current = prev
                prev = temp
                count = 1
                print(current.val)
                print(prev.val)

                current = prev.next

       

a = Node(5)
b = Node(6)
c = Node(7)
d = Node(8)
e = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e

def printList(head):
    current = head 
    while current :
        print(current.val)
        current = current.next


s = Solution()
s.swapNodes(a)



