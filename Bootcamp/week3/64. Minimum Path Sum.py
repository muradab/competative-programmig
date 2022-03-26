# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# [1,3,1]
# [1,5,1]
# [4,2,1]

# result grid  would be like
# [inf, inf, inf, inf]
# [inf, inf, inf, inf]
# [inf, inf, inf, inf]
# [inf, inf, 0, inf]

# go until you reach top corner



class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row ,col = len(grid),len(grid[0])
        
        result = [[float("inf")] * (col+1) for i in range (row+1)]
        
        result[row][col-1] = 0
        
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                result[r][c] = grid[r][c] + min(result[r+1][c],result[r][c+1]) 
                
                
        return result[0][0]
