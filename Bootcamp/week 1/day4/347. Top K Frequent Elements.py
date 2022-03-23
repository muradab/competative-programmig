# Given an integer array nums and an integer k, 
# return the k most frequent elements. You may return the answer in any order.
from typing import List 
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = [] 
        heap = []
        for i in nums :
            if i not in frequency :
                frequency[i] = 1
            else :
                frequency[i] += 1
                
        for f in frequency :
            heapq.heappush(heap , [-frequency[f],f])
                 

        
        
        
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
            
            
            
            
        return result