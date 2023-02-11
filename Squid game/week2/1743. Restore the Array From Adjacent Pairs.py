class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pairs = defaultdict(list)
        for u, v in adjacentPairs:
            pairs[u].append(v)
            pairs[v].append(u)
        start = min(pairs, key =lambda x: len(pairs[x]))
        array = []
        nxt = start
        count = 0
        n =len(adjacentPairs)
        while count <= n:
            if len(pairs[nxt]) == 1:
                array.append(nxt)
                nxt = pairs[start][0]
            else:
                x, y = pairs[nxt]
                newnxt = x if x != array[-1] else y
                array.append(nxt)
                nxt = newnxt
            count += 1
        return array
