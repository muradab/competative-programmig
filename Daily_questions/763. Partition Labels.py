# You are given a string s. We want to partition the string into 
# as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.
from typing import str , List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastApearance = {}
        for i in range(len(s)):
            lastApearance[s[i]] = i
            
        # print(lastApearance)
        
        result = []
        i =  0
        
        while i < len(s):
            ending = lastApearance[s[i]]
            j = i + 1
            while j < ending:
                if lastApearance[s[j]] > ending:
                    ending = lastApearance[s[j]] 
                j += 1
           
            result.append(ending - i + 1)
            i = ending + 1
            
        return result