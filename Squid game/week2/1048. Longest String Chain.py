class Solution:
    def isPredecessor(self, word1: str, word2: str) -> bool:
        if len(word1) + 1 != len(word2) :
            return False
        i = 0
        for c in word2:
            if i == len(word1): return True
            if word1[i] == c:
                i += 1
        return i == len(word1)
    
    def longestStrChain(self, words: List[str]) -> int:
        graph = defaultdict(set)
        words = set(words)
        
        for word in words:
            graph[len(word)].add(word)
            

        @lru_cache(None)
        def dfs(word):
            
            answer = 1 
            
            for nei in graph[len(word)+1]:
                if self.isPredecessor(word, nei):
                    answer = max(answer, 1 + dfs(nei))
                
            return answer
        
        return max(dfs(word) for word in words)
        
        
        
        
