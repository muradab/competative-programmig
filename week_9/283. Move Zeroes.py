# Given an integer array nums, move all 0's to the end of it while maintaining 
# the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
from typing import List 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         index of swaping
        index = 0
    
        for i in range(len(nums)):
            if nums[i] != 0:
                
                nums[index] , nums[i] = nums[i] , nums[index]
                index += 1