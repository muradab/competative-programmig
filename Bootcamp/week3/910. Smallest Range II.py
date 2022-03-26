# You are given an integer array nums and an integer k.

# For each index i where 0 <= i < nums.length, change nums[i] to be either nums[i] + k or nums[i] - k.

# The score of nums is the difference between the maximum and minimum elements in nums.

# Return the minimum score of nums after changing the values at each index.

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = nums[-1] - nums[0]
        for i in range(1,len(nums)):
            result = min(result,max(nums[-1]-k,nums[i-1]+k)-min(nums[0]+k,nums[i]-k))
        return result
        
