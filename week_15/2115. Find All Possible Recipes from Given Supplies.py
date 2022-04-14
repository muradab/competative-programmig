# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        for i,recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
            inDegree[recipe] += len(ingredients[i])
    
        queue =deque ([supply for supply in supplies])
        
        while queue :
            popped = queue.popleft()
            for neighbour in graph[popped]:
                inDegree[neighbour] -= 1
                
                if inDegree[neighbour] == 0 :
                    queue.append(neighbour)
                    
        result = []
        
        for recipe in recipes:
            if inDegree[recipe]==0:
                result.append(recipe)
        return result 
                
        

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            
