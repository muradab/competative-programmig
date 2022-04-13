# https://leetcode.com/problems/course-schedule-iv/
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        
        for course ,pre  in prerequisites :
            graph[pre].append(course)
            
        @lru_cache(None)   
        def dfs (pre , course):
            if graph[course] ==[]:
                return False
            if pre in graph[course]:
                return True
            
            for cour in graph[course]:
                if dfs(pre,cour):
                    return True
            
            return False
        result = [] 
        for course , pre in queries:
            result.append(dfs(course,pre))
            
        return result
