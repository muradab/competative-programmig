class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(element) for element in nums]
        nums.sort()
        
        return  str(nums[-k])