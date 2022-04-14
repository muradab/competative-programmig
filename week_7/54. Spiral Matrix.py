# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        result = []
        i,j ,di ,dj = 0,0,0,1
        n,m= len(matrix),len(matrix[0])
        for _ in range(n*m):
            result.append(matrix[i][j])
            visited.add((i,j))
            if((i+di)%n,(j+dj)%m) in visited:
                di ,dj = dj , -di
                
            i += di
            j += dj
        
        return result
                
        
