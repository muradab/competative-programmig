from typing import List
class Solution:
    def ValidMountainArray(self,arr:List[int])->bool:
        index = 1
        while index < len(arr) and arr[index] > arr[index-1]:
            index += 1
        if index == 1 or index == len(arr):
            return False
        while index < len(arr) and arr[index] < arr[index-1]:
            index += 1
        
        return index == len(arr)
        

s = Solution()
arr = [0,2,3,4,5,2,1]

answer = s.ValidMountainArray(arr)
print(answer)
