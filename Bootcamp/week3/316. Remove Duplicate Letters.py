# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        p = 0
        while p < len(s):
            if not stack :
                stack.append(s[p])

            if stack[-1] < s[p] and s[p] not in stack:
                stack.append(s[p])
                # counter[stack[-1]] -= 1
                
            elif stack[-1] > s[p]:
                while stack and s[p]  not in stack and stack[-1] > s[p] and counter[stack[-1]] > 0 :
                    stack.pop()
                if s[p]  not in stack :    
                    stack.append(s[p])
            
            counter[s[p]] -= 1
                    
            p += 1
            
        return ''.join(stack)
