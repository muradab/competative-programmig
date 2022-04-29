# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode :
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        
        for ch in word :
            if ch not in temp.children :
                temp.children[ch] = TrieNode()
            temp = temp.children[ch]
            
        temp.endOfWord = True

    def search(self, word: str) -> bool:
        temp = self.root
        
        for ch in word :
            if ch not in temp.children:
                return False
            
            temp = temp.children[ch]
            
        return temp.endOfWord

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        
        for ch in prefix :
            if ch not in temp.children:
                return False
            
            temp = temp.children[ch]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
