# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

# It is ().
# It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
# It can be written as (A), where A is a valid parentheses string.
# You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

# If locked[i] is '1', you cannot change s[i].
# But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# Return true if you can make s a valid parentheses string. Otherwise, return false.

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0 :
            return False
        
        can_be_changed = 0
        
        closing_brackets = 0
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(': 
                can_be_changed += 1
            else:
                closing_brackets += 1
                
            # if we can't  create an opening bracket we return false    
            if can_be_changed -  closing_brackets < 0:
                return False 
        
        can_be_changed = 0
        opening_brackets = 0
        for i in range(len(s)-1,-1,-1):
            if locked[i] == '0' or s[i] == ')': 
                can_be_changed += 1
            else:
                opening_brackets += 1
                
            # if we can't  create a closing bracket we return false    
            if can_be_changed -  opening_brackets < 0:
                return False 
       
        return True
