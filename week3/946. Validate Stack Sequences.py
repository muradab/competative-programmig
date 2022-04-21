# https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        count = 0 
        n =  len(pushed)
        for i in range(n):
            stack.append(pushed[i])
            
            while stack and stack[-1] == popped[count]:
                stack.pop()
                count += 1
                
                
        return count == n
