# https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        valids = list(set(words))
        trie = {}
        
        def insert(word):
            temp = trie
            for ch in word :
                if ch not in temp :
                    temp[ch] = {}
                temp = temp[ch]
                
        def isPrefix(word):
            temp = trie
            for ch in word:
                if ch not in temp:
                    return False
                temp = temp[ch]
            return len(temp) != 0
        res = len(valids) 
        for word in valids:
            insert(reversed(word))
            res += len(word)
        
        for word in valids :
            if isPrefix(reversed(word)):
                res -= (len(word) +1)
                
        
        return res
