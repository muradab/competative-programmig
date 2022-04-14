# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        result = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
        
        def dfs(turn , curr):
            for neighbour in graph[curr]:
                if result[neighbour] and result[neighbour][-1] == turn:
                     continue
                result[neighbour].append(turn)
                dfs(turn, neighbour) 

        for i in range(n):
            dfs(i, i)
        return result
        
