# Design a class to find the kth largest element in a stream. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream 
# and returns the element representing the kth largest element in the stream.


from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        
        while len(self.nums) > k :
            heapq.heappop(self.nums)
            
        

    def add(self, val: int) -> int:
        if (self.k > len(self.nums)):
            heapq.heappush(self.nums,val)
            
        elif (val >= self.nums[0]):
            heapq.heappop(self.nums)
            heapq.heappush(self.nums,val)
        
        return self.nums[0]