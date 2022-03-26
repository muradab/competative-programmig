# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

class Solution:
    def __init__(self):
        self.memo = {}
    
    def fib(self, n: int) -> int:
       
        if n in self.memo :
            return self.memo[n]
        if n == 0:
            return 0
        elif n==1 :
            return 1
        else :
            result = self.fib(n-1) 
            self.memo[n-1] = result
            result += self.fib(n-2)
            self.memo[n-2] = result

        return result
            
            
        
