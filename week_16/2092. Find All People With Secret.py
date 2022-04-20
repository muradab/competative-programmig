# https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent = [i for i in range(n)]
        ranks = [1 for _ in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x, y = find(x), find(y)
            if x != y: 
                if ranks[x] < ranks[y]:
                    parent[x] = y
                else:
                    if ranks[x] == ranks[y]:
                        ranks[x] += 1
                    parent[y] = x
        
        graph = defaultdict(list)
        for person1 , person2 , time in meetings:
            graph[time].append((person1, person2))
        

        parent[firstPerson], ranks[firstPerson] = 0, 2
        
        for time ,pairs in sorted(graph.items()):
            visited = set()
            for person1,person2 in pairs:
                visited.add(person1)
                visited.add(person2)
                union(person1,person2)
                
            for num in visited:
                if find(num) != find(0):
                    parent[num] = num
                    
        result = []
        for i in range(n):
            if find(i) == find(0):
                result.append(i)
        return result
