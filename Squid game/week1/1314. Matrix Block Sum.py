class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0 for i in range(cols+1)] for j in range(rows+1)]
        for i in range(rows):
            for j in range(cols):
                prefix[i+1][j+1] = mat[i][j] + prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]
        ans = [[0 for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            lower = min(i+k+1, rows)
            upper = max(i-k, 0)
            for j in range(cols):
                right = min(j+1 + k, cols)
                left = max(j-k, 0)
                answer[i][j] = prefix[lower][right] - prefix[upper][right] - prefix[lower][left] + prefix[upper][left] 
        return answer
                
        
        
