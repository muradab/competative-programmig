class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        
        for c in s:
            if c == '(':
                stack.append('')
                
            elif c == ')':
                # pop the last sum of words
                add = stack.pop()
                
                #reverse the string
                add = add[::-1]
                
                #add it to the tail 
                stack[-1] += add
                
            else:
                stack[-1] += c
          
        return stack.pop()
