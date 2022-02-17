# Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
#  leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Definition for singly-linked list.
from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, current = dummy, head

        while current and current.next:
            if current.val != current.next.val:
                
                prev, current = current, current.next
            else:
               
                while current.next and current.val == current.next.val:
                    current = current.next

             
                prev.next = current.next
                current = current.next

        return dummy.next

        