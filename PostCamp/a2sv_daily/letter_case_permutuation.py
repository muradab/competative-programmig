from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtracking(i, path):
            if i == len(s):
                ans.append(''.join(path))
                return
            
            if s[i].isalpha():
                if s[i].islower():
                    backtracking(i+1, path + [s[i].upper()])
                else:
                    backtracking(i+1, path + [s[i].lower()])
            backtracking(i+1, path+[s[i]])
        
        backtracking(0, [])
        return ans
            
            
