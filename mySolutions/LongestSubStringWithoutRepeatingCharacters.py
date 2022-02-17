class Solution:
    def lengthOfLongestSubstring(self, s:str)->int:
        substring = {}
        left = 0
        right = 0
        count = 0
        while left < len(s) and right < len(s):
            ch = s[right]
            if ch in substring :
                left = max(left,substring[ch]+1)
            substring[ch] = right

            count= max(count,right-left+1)
            right += 1

        return count

s = Solution()
answer = s.lengthOfLongestSubstring('fivestarreview')
print(answer)
                
