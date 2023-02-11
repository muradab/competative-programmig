class Solution:
    def maximumSwap(self, num: int) -> int:
        temp = list(str(num))
        nums = []
        res =''.join(temp)
        for i in range(len(temp)):
            for j in range(i+1, len(temp)):
                temp[i], temp[j] = temp[j], temp[i]
                res = max(res, ''.join(temp))
                temp[i], temp[j] = temp[j], temp[i]
        return int(res)
        
        
