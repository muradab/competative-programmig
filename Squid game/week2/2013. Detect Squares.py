class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.axisPairs = defaultdict(set)
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.axisPairs[y].add(x)
        

    def count(self, point: List[int]) -> int:
        ans = 0
        x, y = point
        for pair in self.axisPairs[y]:
            diff = abs(x - pair)
            if diff == 0:
                continue
            
            if x > pair:
                if (x,y+diff) in self.points and (x-diff, y+diff) in self.points:
                    ans += self.points[(x,y+diff)] * self.points[(x-diff, y+diff)] * self.points[(x-diff, y)]
                if (x,y-diff) in self.points and (x-diff, y-diff) in self.points:
                    ans += self.points[(x,y-diff)] * self.points[(x-diff, y-diff)] * self.points[(x-diff, y)]
            else:
                if (x+diff,y+diff) in self.points and (x, y+diff) in self.points:
                    ans += self.points[(x+diff,y+diff)] * self.points[(x, y+diff)] * self.points[(x+diff, y)]
                if (x,y-diff) in self.points and (x+diff, y-diff) in self.points:
                    ans += self.points[(x,y-diff)] * self.points[(x+diff, y-diff)] * self.points[(x+diff, y)]
        return ans
                
                
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
