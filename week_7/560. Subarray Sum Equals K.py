from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        DictSum = {}
        sum_ = 0
        count = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            DictSum[sum_] = i
            
            if ( sum_ - k)   in DictSum or sum_ - k == 0: 

                count += 1
            print(sum_)
            # print(DictSum)

            
                
        return count

s = Solution()
nums = [1,-1,0]
k = 0
answer = s.subarraySum(nums,k)
print(answer)
                
                