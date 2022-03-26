# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        start = -1
        end = 1
        
        if len(flowerbed) < 3 and flowerbed[0]==flowerbed[-1]==0 and n==1:
            flowerbed[start+1] = 1
            count += 1
        
        if len(flowerbed) > 2 and flowerbed[start+1] == flowerbed[end] == 0:
                flowerbed[start+1] = 1
                count += 1
        
        
        while end <= len(flowerbed):
            if start < 0 and end < len(flowerbed) and flowerbed[start + 1] == flowerbed[end] == 0:
                flowerbed[start+1] = 1
                count += 1
            elif end == len(flowerbed)  and flowerbed[start ] == flowerbed[start + 1] == 0:
                flowerbed[start+1] = 1
                count += 1
            elif end < len(flowerbed) and flowerbed[start] == flowerbed[start + 1] == flowerbed[end] == 0:
                flowerbed[start+1] = 1
                count += 1
                
                
            start += 1
            end += 1 
        
        return count >= n
            
         
