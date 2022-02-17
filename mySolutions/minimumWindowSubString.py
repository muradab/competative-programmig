class Solution:
    def minimumWindowSubString(self, s:str,T:str)->str:
        substring = {}
        left = 0
        right = 0
        count = 0
        while left < len(s)-len(T) and right < len(s):
            ch = s[right]
            if ch in T :
                left = max(left,substring[ch]+1)
            substring[ch] = right

            count= max(count,right-left+1)
            right += 1

        return count

s = Solution()
answer = s.minimumWindowSubString('fivestarreview',"five")
print(answer)
                
