# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost) 
        memo = {}
        def helper(position):
            if position in memo :
                return memo[position]
            if position < 2:
                return   cost[position]            
            jump = helper(position - 2)
            nojump = helper(position - 1 )
            
            memo[position] = min(jump,nojump) + cost[position]
            
            return memo[position]
            
            
        cost.append(0)
        return helper(length)
        
