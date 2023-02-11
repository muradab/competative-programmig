from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list, record = self.get_adj_record(equations, values)
        ans = []
        for q in queries:
            start, end = q[0], q[1]
            if start == end and start in adj_list:
                ans.append(1.0)
                continue
            queue, res, visited = deque(), -1.0, set()
            queue.append((start, 1.0))
            while queue :
                cur_node, cur_val = queue.popleft()
                visited.add(cur_node)
                for nb in adj_list[cur_node]:
                    if nb in visited:
                        continue
                    new_val = cur_val * record[(cur_node, nb)]
                    if nb == end:
                        res = new_val
                        break
                    queue.append((nb, new_val))
            ans.append(res)
        return ans
    def get_adj_record(self, equations, values):
        adj_list, record = defaultdict(list), defaultdict(float)
        for i in range(len(equations)):
            u, v = equations[i]
            adj_list[u].append(v)
            adj_list[v].append(u)
            record[(u, v)] = values[i]
            record[(v, u)] = 1 / values[i]
        return adj_list, record
