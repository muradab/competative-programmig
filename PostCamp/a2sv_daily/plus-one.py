from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ans = []
        for num in reversed(digits):
            ans.append((num + carry)%10)
            carry = (num + carry)//10
        if carry:
            ans.append(carry)
        return ans[::-1]