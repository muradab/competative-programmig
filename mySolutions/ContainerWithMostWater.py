from typing import List 
class Solution :
    def ContainerWithMostWater(self,levels:List[int])-> int:
        left = 0
        right = len(levels) -1
        max_area = 0
        while (left < right):
            max_area = max(max_area,min(levels[left],levels[right])*(right-left) )

            if levels[left]<levels[right]:
                left += 1
            else :
                right -= 1
            
        return max_area

s= Solution()
answer = s.ContainerWithMostWater([1,8,6,2,5,4,8,3,7])
print(answer)
            
        
