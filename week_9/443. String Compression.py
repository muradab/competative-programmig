# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead,
#  be stored in the input character array chars. Note that group lengths 
# that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.
from typing import List 
class Solution:
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0, 0
        while fast < len(chars):
		
            chars[slow] = chars[fast]
            count = 1
			
            while fast + 1 < len(chars) and chars[fast] == chars[fast+1]:
                fast += 1
                count += 1
                

            if count > 1:
                # to split group length
                for c in str(count):
                    chars[slow+1] = c
                    slow += 1
            
            fast += 1
            slow += 1
        
        return slow
            
        