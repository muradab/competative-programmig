# Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.
from typing import List 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # if we jumped self thats equal to multiplying it by one
        answer =  [1] * len(nums)
        
        # answer is left product * right product
        
#         first keep the left product
        product = 1 
        for i in range(len(nums)):
            answer[i] = product
            product *= nums[i]
        
        
#       now multiply the right product to the output you get above
        product = 1
        for i in range(len(nums)-1 ,-1 ,-1): 
            answer[i] *= product
            product *= nums[i]
        return answer  

solution = Solution()
list = [1,2,5,6,8,9,10,11,0]

s = solution.productExceptSelf(list)
print(s)
            