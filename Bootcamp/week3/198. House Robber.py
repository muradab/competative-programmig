# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def helper(i) :
            if i in dp :
                return dp[i]
            if i >= len(nums):
                dp[i] = 0
                return dp[i]
            elif i == len(nums)-1:
                dp[i] = nums[i]
                return dp[i] 
            
            first = nums[i] + helper(i+2) 
            second = helper(i+1)
            dp[i]= max(first,second)
            return dp[i]
            
        return helper(0)
   
#         if len(nums)==1:
#             return nums[0]
        
        
#         first =  0
#         second = 0
        
#         for i in range (len(nums)):
#             temp = max( first + nums[i],second)
#             first = second
#             second = temp
            
#         return second
