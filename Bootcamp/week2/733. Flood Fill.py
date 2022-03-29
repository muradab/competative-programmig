# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

# Return the modified image after performing the flood fill.

# from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.start_color = image[sr][sc]
        self.ROW = len(image)
        self.COL = len(image[0])
        self.newColor = newColor
        self.image = image
        self.visited = set()
        self.DIR = [(-1,0),(1,0),(0,-1),(0,1)]
        
        
        self.dfs(sr,sc)
    
        return self.image
#              
    def isValid(self,r,c):
        if r < 0 or r == self.ROW  or c < 0 or c == self.COL or self.image[r][c] != self.start_color :
            return False
        return True

    def dfs (self,r,c):

        if not self.isValid(r,c) or (r,c) in self.visited :
            return 
        
        self.visited.add((r,c))
        self.image[r][c] = self.newColor

        for dir in self.DIR:
            self.dfs(r+dir[0],c+dir[1])


        # up = self.dfs(r-1,c)
        # down = self.dfs(r+1,c)
        # left = self.dfs(r,c-1)
        # right = self.dfs(r,c+1)

