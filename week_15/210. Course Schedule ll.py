# https://leetcode.com/problems/course-schedule-ii/submissions
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        answer =   []
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        def dfs(course):
            answer.append(course)
            indegree[course] = -1
            for nextCourse in graph[course]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0: 
                    dfs(nextCourse)            
        for course in range(numCourses):
            if indegree[course] == 0:
                dfs(course)

        return answer if len(answer) == numCourses else []
