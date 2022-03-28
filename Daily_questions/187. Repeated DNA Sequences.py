# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        diff = set()
        result = []
        print(length)
        if length <= 10 :
            return result
        counter = DefaultDict(int)
        
        for i in range(length-9):
            counter[s[i:i+10]] += 1
            if counter[s[i:i+10]] > 1 :
                diff.add(s[i:i+10])
        print(counter)        
        for res in diff :
            result.append(res)
                
        return result
