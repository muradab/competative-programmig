# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        lmax = [0] * len(height)
        rmax = [0] * len(height)
        # find the left maximum for each index
        curmax = height[0]
        for i in range(1 , len(height)):            
            lmax[i] = curmax
            curmax = max(curmax,height[i])
       
        # find the right miximum for each index
        curmax = height[-1]
        for i in range(len(height) - 2,-1,-1):            
            rmax[i] = curmax
            curmax = max(curmax,height[i])
        
        # use the formula and find the water to be found
        # min (lmax[i] , rmax[i]) - height[i]
        water = 0
        for i in range(len(height)):
            trapped = min (lmax[i] , rmax[i]) - height[i]
            if trapped > 0:
                water  += trapped
                  
        return water
