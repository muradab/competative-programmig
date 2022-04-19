# https://leetcode.com/problems/min-cost-to-connect-all-points/

class DisJointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1]*size
        
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x != y:
            if self.rank[x] < self.rank[y]:
                x ,y = y , x
            
            self.parent[y] = x
            self.rank[x] += self.rank[y]
            return True
        return False
                
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        djs = DisJointSet(len(points))
        heap = [] 
        for p1 in range(len(points)-1):
            for p2 in range(p1 + 1 ,len(points) ):
                x1 , y1 = points[p1]
                x2 , y2 = points[p2]
                val = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(heap,(val,p1,p2))
        connected = 0
        cost = 0
        while heap and connected < len(points) - 1:
            edge , p1 ,p2 = heapq.heappop(heap)
            if djs.union(p1,p2):
                connected += 1
                cost += edge
                
        return cost
