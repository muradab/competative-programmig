class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        floor = len(nums)// 3
        array = []
        start = nums[0]
        count = 0
        
        for i in range (len(nums)):
            if start == nums[i]:
                count += 1
            else : 
                count = 1
                start = nums[i]
                
            if count > floor :
                if start not in array:
                    array.append(start)
                
        return array