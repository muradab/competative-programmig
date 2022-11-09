from collections import Counter
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        distnict = Counter(nums)
        missing = None
        doubled = None
        for i in range(1,len(nums)+1):
            if i not in distnict:
                missing = i
            
            if distnict[i] == 2:
                doubled = i
            
            
        return [doubled, missing]