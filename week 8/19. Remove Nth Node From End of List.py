from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use two pointers namely fast and slow pointing first index
        
        fast = slow = head
        
        #move ahead the fast pointer by n
        for i in range(n):
            fast = fast.next
            
        # check if fast is at the end    
        if not fast:
            return head.next
        
        # until faast is none
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        
        return head
            
            
        
      
   
    
            
        