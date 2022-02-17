# Given an array, rotate the array to the right by k steps, where k is non-negative.
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0] * len(nums)
        for i in range(len(nums)):
            temp[(i+k)%len(nums)] = nums[i] 

        for i in range(len(nums)):
            nums[i] = temp[i]