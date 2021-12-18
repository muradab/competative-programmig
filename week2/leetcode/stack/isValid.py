class Solution:
    def isValid(self, s: str) -> bool:
        
        openingBrackets = ['(','[','{']
        closingBrackets = [')',']','}']
        stack = []
        balanced = False
        if s[-1] in openingBrackets:
            return False
        
        for i in s :
            if i in openingBrackets:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                else :
                    
                    popped = openingBrackets.index(stack[-1])
                    if closingBrackets.index(i) == popped:
                        stack.pop()
                        balanced = True
                        
                    else :
                        return False
            if len(stack)!=0:
                    balanced = False
        return balanced