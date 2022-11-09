from collections import Counter
from typing import List
class Solution:
    def backtracking(self, customer, quantity: List[int], bucket: List[int]) -> bool:
        if customer == len(quantity):
            return True
        
        for b in range(len(bucket)):
            if bucket[b] >= quantity[customer]:
                bucket[b] -= quantity[customer]
                if self.backtracking(customer+1):
                    return True
                bucket[b] += quantity[customer]
        
        return False

    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        integers = Counter(nums)
        count = sorted(integers.values())[::-1]
        quantity.sort(reverse = True)

        
        return self.backtracking(0, quantity, count)