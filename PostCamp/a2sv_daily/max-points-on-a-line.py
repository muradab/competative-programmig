from collections import defaultdict
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        total lines if the points are on a circle and each points are not in a same line
        a = n - 1 + 1
        b = n - 2
        . =  
        .
        .
        x = 1 + n - 1
        total lines = n^2 / 2
        300 300 90000/2 45 000

        
        
        """

        lines = defaultdict(int)
        maxPoints = 1
        for i in range(len(points)-1):
            x1, y1 = points[i]
            lines = defaultdict(int)
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                b = y2 - y1
                if x1 == x2:
                    lines['und'] += 1
                else:
                    slope = (y2-y1) / (x2-x1)
                    lines[slope] += 1
            
            maxPoints = max(maxPoints, 1 + max(lines.values()))
                    
        return maxPoints
                







