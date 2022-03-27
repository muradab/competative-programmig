# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_ = {}
        
        start = 0
        end = 0
        answer = 0
        max_ = 0
        
        while end < len(s):
            if s[end] in dict_:
                dict_[s[end]] += 1
            else :
                dict_[s[end]] = 1
                
            max_ = max(max_,dict_[s[end]])
            
            while (end-start+1) - max_ > k:
                dict_[s[start]] -= 1
                start += 1
            
            answer = max(answer,end-start+1)
            end += 1
            
        return answer

