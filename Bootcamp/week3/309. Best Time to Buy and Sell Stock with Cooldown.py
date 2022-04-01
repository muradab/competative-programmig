# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def helper(day,buy):
            if (day,buy) in dp :
                return dp[(day,buy)]
            if day >=len(prices) :
                return 0
            
            choice1 = helper(day + 1,buy)
            if buy:
                choice2 = helper(day + 1,False) - prices[day]
            else :
                choice2 = helper(day + 2,True) + prices[day]
            
            
            dp[(day,buy)] =  max(choice1,choice2)
            
            return dp[(day,buy)]
            
        return helper(0,True)
            
                
                
            
