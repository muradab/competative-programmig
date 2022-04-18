# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        nums.sort()
        
        node = answer = ListNode(nums[0])
        
        for i in range(1,len(nums)):
            node.next = ListNode(nums[i])
            node = node.next
        return answer
