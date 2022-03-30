# Given n orders, each order consist in pickup and delivery services. 

# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

# Since the answer may be too large, return it modulo 10^9 + 7.

class Solution:
    def countOrders(self, n: int) -> int:
        def helper (n):
            if n==1:
                return 1
            sum_ = 0
            for i in range(1,2 * (n-1) + 2 ):
                sum_ += i
                
            return (helper(n-1) * sum_) 
        
        return (helper(n) % (10 ** 9 + 7))
        
