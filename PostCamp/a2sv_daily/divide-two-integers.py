class Solution:
    def subtractions(self, dividend, divisor):
        count = 1
        while divisor<<1 < dividend:
            #increase divisor
            divisor <<= 1
            #count divisors
            count <<= 1
        left_over = dividend - divisor
        return left_over, count

    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend >= 0) != (divisor>= 0)
        
        # work with positive numbers
        dividend, divisor = abs(dividend), abs(divisor)

        res = 0
        while divisor <= dividend:
            dividend, count = self.subtractions(dividend, divisor)
            res += count

        if sign:
            return -res
        
        return min(res,2147483647)

        