class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        array = [intervals[0]]
        for i in range (len(intervals)):
            if array[-1][1] >= intervals[i][0]:
                array[-1][1] = max(array[-1][1],intervals[i][1])
                
            else :
                array.append(intervals[i])
                
        return array
                