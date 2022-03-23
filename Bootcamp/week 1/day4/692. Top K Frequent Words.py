# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest.
# Sort the words with the same frequency by their lexicographical order.
import heapq
from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}
        result = [] 
        heap = []
        for i in words :
            if i not in frequency :
                frequency[i] = 1
            else :
                frequency[i] += 1
                
        for f in frequency :
            heapq.heappush(heap , [-frequency[f],f])
                 

        
        
        
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
            
            
            
            
        return result