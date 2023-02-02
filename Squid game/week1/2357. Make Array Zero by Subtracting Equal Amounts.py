class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heapify(nums)
        while nums and not nums[0]:
            heappop(nums)
        subtraction = 0
        ans = 0
        while nums:
            subtraction += (nums[0]-subtraction)
            while nums and nums[0] - subtraction <= 0:
                heappop(nums)
            ans += 1
        return ans
