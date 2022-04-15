# https://leetcode.com/problems/max-area-of-island/
class DJS :
    def __init__ (self):
        self.parent = {}
        self.rank = {}
        
    def find(self,cell):
        if self.parent[cell] != cell :
            return self.find(self.parent[cell])
        return cell
        
    def union(self,cell1 , cell2):
        cell1 , cell2 = self.find(cell1),self.find(cell2)
        if cell1 == cell2 :
            return 

        if self.rank[cell1] > self.rank[cell2]:
            self.parent[cell2] = cell1
            self.rank[cell1] += self.rank[cell2]
        else :
            self.parent[cell1] = cell2
            self.rank[cell2] += self.rank[cell1]
    def setParent (self,cell):
        self.parent[cell] = cell
    def setRank (self,cell):
        self.rank[cell] = 1
    
    def maxRank (self):
        if self.rank.values() :
            return max(self.rank.values())
        return 0
        
    
        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: 
        djs =  DJS()
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j]:
                    cell = (i,j)
                    djs.setParent(cell)
                    djs.setRank(cell)
                    if i - 1 >= 0 and grid[i-1][j]:
                        djs.union(cell,(i-1,j))
                        
                    if j-1 >= 0 and grid[i][j-1]:
                        djs.union(cell,(i,j-1))
        
        return djs.maxRank()
        
