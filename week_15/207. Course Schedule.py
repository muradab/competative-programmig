# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        for i in range (numCourses):
            graph[i] = []
            
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
        
        visited = set()
        
        def dfs(course):
            # if it doesn't require any prerequisite
            if graph[course] == []:
                return True
            # if it's already visited 
            if course in visited :
                return False
            visited.add(course)
            for prerequsite in graph[course]:
                if not dfs(prerequsite):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            
            
        
            
