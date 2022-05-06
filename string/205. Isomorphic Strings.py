# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pairs = {}
        n = len(s)
        for i in range (len(s)):
            if s[i] not in pairs :
                if t[i] in pairs.values():
                    return False
                pairs[s[i]] = t[i]
            elif pairs[s[i]] != t[i]:
                    return False
        return True 
