class Solution:
    def validPalindrome(self, s: str) -> bool:
        def verify(left, right, used):
            if left >= right:
                return True
            if s[left] == s[right]:
                return verify(left+1, right-1, used)
            if not used and s[left] != s[right]:
                return verify(left+1, right, True) or verify(left, right-1, True)
            return False
        return verify(0, len(s)-1, False)
        
        
