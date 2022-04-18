# https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next :
            
            return head
        
        # backup original pointer
        next_node, next_segment = head.next, head.next.next

        # reverse linkage of current pair
        next_node.next = head
        
        # reverse next pair and get the node of current head's next node
        head_next = self.swapPairs(next_segment)
        
        # update linkage from current pair to next pair
        head.next = head_next
        
        return next_node
            
