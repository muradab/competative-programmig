# Given an n x n matrix where each of the rows and columns is sorted in ascending order, 
# return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).
from typing import List
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result = []
        heap = []
        
        for i in range(len(matrix)):
            if matrix[i] :
                heapq.heappush(heap,[matrix[i][0],i])
        
        i = 0
        while(i < k and heap):
            temp = heapq.heappop(heap)
            smallest = temp[0]
            matrix[temp[1]].pop(0)
            
            if (len(matrix[temp[1]]) > 0 ):
                
                
                heapq.heappush(heap,[matrix[temp[1]][0],temp[1]])
                
                
            i += 1