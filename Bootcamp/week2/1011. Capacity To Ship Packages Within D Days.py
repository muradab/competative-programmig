# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            day = 1
            current_weight = 0
            
            for weight in weights:
                if current_weight + weight > mid:
                    day += 1
                    current_weight = 0
                current_weight += weight
           
            if day > days:
                left = mid + 1
            else:
                right = mid
        return left
