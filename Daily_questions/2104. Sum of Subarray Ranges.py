# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

# Return the sum of all subarray ranges of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
                
#         brute force
        result = 0
        for i in range(len(nums)-1):
            max_ = nums[i]
            min_ = nums[i]
            
            for j in range(i+1,len(nums)):
                max_ = max(max_,nums[j])
                min_ = min(min_,nums[j])
                result += max_ - min_
                
        return result
