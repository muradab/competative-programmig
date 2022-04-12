class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]: 
        visited = set()
        
        def dfs (i):
            if i in visited:
                return False
            
            if graph[i] == []  :
                return True
            
            visited.add(i)
            
            for node in graph[i]:
                if not dfs(node):
                    return False
            visited.remove(i)
            graph[i] = []
                
            return True
        answer = []    
        for i in range(len(graph)):
            if dfs(i):
                answer.append(i)
       
        return answer
                
                
                
        
