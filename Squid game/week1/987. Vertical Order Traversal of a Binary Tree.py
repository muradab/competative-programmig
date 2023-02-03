# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.heap = []
        def dfs(root, row, col):
            if root:
                dfs(root.left, row+1, col-1)
                heappush(self.heap, (col,row,root.val))
                dfs(root.right, row+1, col + 1)
                
        dfs(root, 0, 0)
        
        answer = [[]]
        start = self.heap[0][0]
        while self.heap:
            col, _ , node = heappop(self.heap)
            if col != start:
                start = col
                answer.append([])
            answer[-1].append(node)
            
        return answer         
        
