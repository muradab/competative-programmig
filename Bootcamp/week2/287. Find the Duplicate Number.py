# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        
        def counter(mid):
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            
            return count
            
            
        
        while left <= right:
            
            mid = left + (right-left) // 2
            
            
            if counter(mid) > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left
