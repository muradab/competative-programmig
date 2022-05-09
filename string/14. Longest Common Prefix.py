# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        my_sorted_list = sorted(strs, key=lambda el: len(el))
        prefix = my_sorted_list[0]
        for word in my_sorted_list[1:]:
            for i in range (len(prefix)):
                if not prefix:
                    return '' 
                if word[i] != prefix[i]:
                    prefix = prefix[0:i]
                    break
        return prefix
                
