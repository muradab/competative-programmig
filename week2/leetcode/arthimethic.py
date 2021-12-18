class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i in range (len(l)):
            sliced = nums[l[i]:r[i]+1]

            sliced.sort()
            
            diff = sliced[1] - sliced[0]
            for k in range(1,len(sliced)):
                newDiff = sliced[k] - sliced[k-1]
                if newDiff != diff :
                    output.append(False)
                    break
                if k == len(sliced)-1:
                    output.append(True)
                        
        return output
        