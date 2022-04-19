# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n, cycle = len(favorite), 0
        seen = set()
        
        # find the maximum cycle
        for employee in range(n):
            if employee not in seen:
                start = employee
                currentPerson = employee
                currentVisited = set()
				
            while currentPerson not in seen:
                seen.add(currentPerson)
                currentVisited.add(currentPerson)
                currentPerson = favorite[currentPerson]
               
              # calculate the new cycle if it is in current set
                if currentPerson in currentVisited:      
                    employees = len(currentVisited)
                    
                    # find where does it began
                    while start != currentPerson:
                        employees -= 1
                        start = favorite[start]
                    cycle = max(cycle, employees)
        
        # find mutual favorites
        pair = []
        visited = set()
        for i in range(n):

            if favorite[favorite[i]] == i and i not in visited:
                pair.append([i, favorite[i]])
                visited.add(i)
                visited.add(favorite[i])
		
        result = 0
        
        
        # create the graph
        graph = collections.defaultdict(list)
        for i in range(n):
            graph[favorite[i]].append(i)
        
        
        
        # find longest path from each direction
        def bfs(one,two):
            max_ = 0
            deque = collections.deque()
            for employee in graph[one]:
                if employee != two:
                    deque.append([employee, 1])
            while deque:
                cur, n = deque.popleft()
                max_ = max(max_, n)
                for nxt_employee in graph[cur]:
                    deque.append([nxt_employee, n + 1])
            return max_
        
        
        # find mutual favorites
        for a , b in pair:
            result1 = bfs(a,b)
            result2 = bfs(b,a)
            result += 2 + result1 + result2
        
        
        
        return max(cycle, result) 
