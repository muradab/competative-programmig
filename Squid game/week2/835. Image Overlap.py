class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ans = 0
        first = []
        for i, row in enumerate(img1):
            for j,num in enumerate(row):
                if num:
                    first.append((i, j))
        
        second = []
        for i, row in enumerate(img2):
            for j,num in enumerate(row):
                if num:
                    second.append((i, j))
        
        translate = defaultdict(int)
        for r1, c1 in first:
            for r2, c2 in second:
                vector = (r1 - r2, c1 - c2)
                translate[vector] += 1
                ans = max(ans, translate[vector])
        
        return ans
                
        
        
