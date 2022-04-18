# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        
        while head : 
            nums.append(head.val)
            head = head.next
            
        result = 0
        left ,right = 0 ,len(nums) - 1
        while left < right:
            result = max(result , nums[right]+ nums[left])
            
            left += 1
            right -= 1
            
        return result
        
