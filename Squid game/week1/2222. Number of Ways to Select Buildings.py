class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros, ones = 0, 0
        ans = 0
        zero_one = 0
        one_zero = 0
        for ch in s:
            if ch == '0':
                zeros += 1
                one_zero += ones
                ans += zero_one
            else:
                ones += 1
                zero_one += zeros
                ans += one_zero
        return ans
                
