class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distnict = list(set(x for x in nums))
        
        if len(distnict)<3:
            return max(distnict)
        
        distnict.sort()
        return distnict[-3]
