# https://leetcode.com/problems/parallel-courses-iii/submissions/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        for prv, nxt in relations:
            graph[prv].append(nxt)
            inDegree[nxt] += 1

        queue = deque()
        finishMonth = [0] * (n+1)
        for i in range(1,n+1):
            if inDegree[i] == 0:
                queue.append(i)
                finishMonth[i] = time[i-1]

        while queue:
            popped = queue.popleft()
            for course in graph[popped]:
                finishMonth[course] = max(finishMonth[popped] + time[course-1],
                                          finishMonth[course])  
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)
        return max(finishMonth)
        
