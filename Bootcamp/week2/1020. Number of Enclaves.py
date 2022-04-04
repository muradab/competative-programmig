# https://leetcode.com/problems/number-of-enclaves/


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        DIR = [(-1,0),(1,0),(0,-1),(0,1)]
        # do dfs on boundary 1's and count the left 1s that are not changed
        def dfs (row,col):
            if inBound(row,col) and grid[row][col] == 1:
                grid[row][col] = 0
                for d in DIR :
                    dfs(row + d[0],col + d[1])
            
        # helper functions  inbound and onboundary
        
        def inBound(row,col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                return True
            return False
        
        def onBoundary(row,col):
            if row == 0 or row == len(grid)-1 or col == 0 or col == len(grid[0])-1:
                return True
            return False
        
        #call dfs on boundary
        for row in range (len(grid)):
            for col in range (len(grid[0])):
                if onBoundary(row,col):
                    dfs(row,col)

        # count the 1's left
        answer = 0
        
        for row in range (len(grid)):
            for col in range (len(grid[0])):
                if grid[row][col] == 1:
                    answer += 1
        
        
        return answer
                
        
