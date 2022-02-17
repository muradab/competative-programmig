import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
       
       
       
        for i in tokens :
            is_positive_integer = i.isdigit()
            is_negative_integer =  i.startswith("-") and i[1:].isdigit()
            is_integer = is_positive_integer or is_negative_integer
            if  (is_positive_integer or is_negative_integer ):
                stack.append(int(i))
            
            else :
                
                result = eval(f"{int(stack[-2])} {i} {int(stack[-1])}")
               
                if result < 0:
                    result = math.ceil(result)
                else :
                    result = math.floor(result)
                stack.pop()
                stack.pop()
                stack.append(result)
           
                
        return stack[0]
        