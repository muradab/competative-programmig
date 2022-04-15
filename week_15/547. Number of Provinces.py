# https://leetcode.com/problems/number-of-provinces/

class DisJointSet:
    def __init__(self,cities):
        self.parent = [i for i in range(cities)]
        self.provinces = cities
    
    def find(self,city):
        if self.parent[city] != city:
            return self.find(self.parent[city])
        return self.parent[city]
    
    def union(self,city1,city2):
        city1,city2 = self.find(city1),self.find(city2)
        if city1 != city2:
            self.parent[city2] = city1
            self.provinces -= 1
    
    def provinces(self):
        return self.provinces
    
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        djs = DisJointSet(cities)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i != j and isConnected[i][j] :
                    djs.union(i,j)
        return djs.provinces
    
