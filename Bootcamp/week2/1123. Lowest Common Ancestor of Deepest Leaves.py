# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node,depth):
            nonlocal answer , maxDepth
            maxDepth = max( maxDepth ,depth)
            if not node :
                return  depth
            
            left = dfs(node.left , depth + 1)
            right = dfs (node.right , depth + 1)
            
            if left == right == maxDepth:
                answer = node
            
            return max(left,right)
        maxDepth = 0
        answer = None
        dfs (root,0)
        
        return answer
