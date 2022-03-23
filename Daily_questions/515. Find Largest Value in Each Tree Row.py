# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
# Definition for a binary tree node.

from typing import Optional , List
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.level = 0

        def dfs (root , row ):
            if not root :
                return 

            if row == self.level :
                self.level += 1
                result.append(root.val)
                

            if root.val > result[row] :
                result[row] = root.val 
                

            dfs(root.left , row+1)
            dfs(root.right , row +1)

        dfs(root , 0)

        return result

# Tree = TreeNode(-2)
# Tree.left = TreeNode(5)
# Tree.right = TreeNode(3)
# Tree.left.left = TreeNode(9)
# Tree.left.right = TreeNode(4)
# Tree.right.left = TreeNode(2)
# Tree.right.right =  TreeNode(15)
# Tree.left.left.left = TreeNode(8)
# Tree.left.left.right = TreeNode(6)
# Tree.left.right.left = TreeNode(2)
# Tree.left.right.right = TreeNode(1)
# Tree.right.left.left = TreeNode(12)
# Tree.right.left.right = TreeNode(13)
# Tree.right.right.left =  TreeNode(20)
# Tree.right.right.right =  TreeNode(2)

# s = Solution()
# print(s.largestValues(Tree))