# Given an array of integers nums and an integer k. 
# A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

from typing import List 
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        preCount = {}
    
        preCount[0] = 1
        answer = 0
        count = 0
        for num in nums:
            
            if num % 2 != 0:
                count += 1
                preCount[count] = 0
                
            preCount[count] += 1
            
            
            if count - k in preCount:
                answer += preCount[count - k]
            print(preCount)
            print(answer)
        return answer

solution = Solution()
list = [1,2,5,6,9,10,11,0]

s = solution.numberOfSubarrays(list,2)
print(s)