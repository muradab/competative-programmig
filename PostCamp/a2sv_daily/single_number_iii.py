from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
            
        # merge them bases on the bits they differ
        
        shift = 0
        while not (xor & 1):
            if shift == 32:
                break
            shift += 1
            xor >>= 1
            
            
        
        x1,x2 = 0, 0
        for num in nums:
            if num & (1<< shift):
                x1 ^= num
            else:
                x2 ^= num
        return [x1, x2]