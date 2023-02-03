class Solution:

    def __init__(self, w: List[int]):
        self.weight = w
        for i in range(1, len(self.weight)):
            self.weight[i] += self.weight[i-1]
    def pickIndex(self) -> int:
        random_weight =  random.randint(1, self.weight[-1])
        return bisect_left(self.weight, random_weight)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
