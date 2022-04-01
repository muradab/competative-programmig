# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit =set()
        queue = []
        DIR = [(-1,0),(1,0),(0,-1),(0,1)]
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visit.add((i, j))
                elif grid[i][j] == 2:
                    queue.append((i, j))
        result = 0
        while visit and queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)  
                for d in DIR:
                    cell = (i +d[0] , j + d[1])
                    if cell in visit:  
                        visit.remove(cell)
                        queue.append(cell)
            result += 1
		
        return -1 if visit else result
            
