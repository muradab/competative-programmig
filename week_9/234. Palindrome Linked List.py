# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        
        while head :
            stack.append(head.val)
            head = head.next
        
        left ,right = 0 ,len(stack) - 1
        while left < right :
            if stack[left] != stack[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
    
#  # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         prev = None
#         slow = fast = head
        
#         while fast and  fast.next :
#             fast = fast.next.next
#             prev , prev.next , slow = slow , prev , slow.next
        
#         if fast :
#             slow = slow.next
        
#         while prev and slow.val == prev.val :
#             slow = slow.next
#             prev = prev.next
        
#         return not slow
