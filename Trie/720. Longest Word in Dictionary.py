# https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie , result = {} ,""
        words.sort()
        
        def prefix (word):
            temp = trie
            for ch in word :
                if ch not in temp :
                    return False
                temp = temp[ch]
            return True
        
        def insert(word):
            temp = trie
            for ch in word:
                if ch not in temp :
                    temp[ch] = {}
                temp = temp[ch]
        
        for word in words:
            n = len(word)
            if n == 1 or prefix(word[0:n-1]) :
                if n > len(result): result = word
                insert(word)
        return result
