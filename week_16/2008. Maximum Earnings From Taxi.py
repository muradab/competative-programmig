# https://leetcode.com/problems/maximum-earnings-from-taxi/

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(index):
            if index >= len(rides):
                return 0
            start , end , tip = rides[index]
            next_index = binarySearch(index)
            pick_up = end - start + tip + dp(next_index)
            leave = dp(index + 1)
            
            
            return max(pick_up,leave)
        def binarySearch(index):
            left = index + 1
            right = len(rides)-1
            end = rides[index][1]
            while left <= right:
                mid = left + (right - left) // 2
                if rides[mid][0] < end :
                    left = mid + 1
                else :
                    right = mid -1
            return left
                    
        rides.sort()
        return dp(0)    
            
        
