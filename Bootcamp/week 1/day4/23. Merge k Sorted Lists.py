# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.
from typing import Optional,List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode()
        current = head
        
        heap = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(heap,[lists[i].val,i])
            
        while(heap):
            temp = heapq.heappop(heap)
            current.next = lists[temp[1]]
            if (lists[temp[1]].next ):
                lists[temp[1]] = lists[temp[1]].next
                heapq.heappush(heap,[lists[temp[1]].val,temp[1]])
            current = current.next
        return head.next
    
        