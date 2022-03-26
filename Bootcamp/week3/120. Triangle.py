# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
#         length = len(triangle)
#         # memo = {}
        arr = triangle[-1][:]
     
        for i in reversed(range(len(triangle)-1)):
            for index in range(len(triangle[i])):
                arr[index] = triangle[i][index] + min(arr[index],arr[index+1])
            
        return arr[0]
      
#       top down approach
            
#         def helper (index,level):
            
#             if(index,level) in memo :
#                 return memo[(index,level)]
            
            
#             if level == length - 1 :
#                 return (triangle[level][index])
            
#             down = helper(index,level+1)
#             right = helper(index+1,level+1)
            
            
#             path = min(down,right) + triangle[level][index]
#             memo[(index,level)] = path
            
#             return memo[(index,level)]
        
        
        # return helper(0,0)
